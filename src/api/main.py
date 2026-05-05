from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional
import logging

from src.retrieval.retriever import build_retriever
from src.generation.chain import generate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
        title="Grounded RAG API",
)

retriever = build_retriever()

class AskRequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=500)


class SourceItem(BaseModel):
    filename: str
    section: str
    similarity_score: float

class AskResponse(BaseModel):
    answer: str
    sources: List[SourceItem]


class ErrorResponse(BaseModel):
    error: str
    message: str
    status: str = "error"


@app.post("/ask", response_model=AskResponse)
def ask(req:AskRequest):
    try:

        if not req.question.strip():
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "Question cannot be empty"
            )

        chunks = retriever(req.question)
        result = generate(req.question, chunks)

        sources = []
        for s in result.get("sources", []):
            try:
                sources.append(SourceItem(
                    filename=s.get("filename", "unknown.md"),
                    section=s.get("section", "Root"),
                    similarity_score=float(s.get("similarity_score", 0.0))
                ))

            except (TypeError, ValueError) as e:
                logger.warning(f"Skipping malformed source item: {e}")
                continue

        return AskResponse(
                answer = result["answer"],
                sources = [SourceItem(**s) for s in result.get("sources", [])]
        )
    
    except ValidationError as e:
        logger.error(f"Request validation error: {e}")
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=ErrorResponse(
                error="validation_error",
                message="Invalid request format"
            ).model_dump()
        )
    except Exception as e:
        logger.error(f"Unexpected pipeline error: {e}", exc_info=True)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=ErrorResponse(
                error="internal_error",
                message="RAG pipeline failed. Check server logs."
            ).model_dump()
        )


# Add to src/api/main.py
@app.get("/debug/retrieve")
def debug_retrieve(q: str):
    """Debug: see raw retrieved chunks + scores"""
    chunks = retriever(q)  # Your existing retriever function
    if chunks is None:
        return {"query": q, "retrieved": None, "reason": "below_threshold_or_empty"}
    return {
        "query": q,
        "count": len(chunks),
        "chunks": [
            {
                "filename": c["filename"],
                "section": c["section"],
                "score": c["similarity_score"],
                "preview": c["page_content"][:200] + "..."
            }
            for c in chunks
        ]
    }

@app.get("health_check")
def health():
    return {
        "status": "healthy",
        "service": "grounded rag api"
    }