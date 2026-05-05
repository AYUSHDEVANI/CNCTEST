from pydantic import BaseModel, Field
from typing import List

class SourceCitation(BaseModel):
    filename: str
    section: str
    similarity_score: float

class RAGResponse(BaseModel):
    answer: str = Field(
        description="Direct, concise answer grounded ONLY in provided context."
    )
    sources: List[SourceCitation] = Field(
        description="Exact files/sections used to generate the answer."
    )