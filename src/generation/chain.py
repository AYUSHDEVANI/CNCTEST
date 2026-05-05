from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnablePassthrough
from pydantic import ValidationError
import logging

from src.config import GROQ_API_KEY, GROQ_MODEL
from src.utils.schema import RAGResponse

logger = logging.getLogger(__name__)

if not GROQ_API_KEY:
    raise ValueError("GROQ API KEY not assigned")

llm = ChatGroq(
        model = GROQ_MODEL,
        temperature = 0.3,
        api_key = GROQ_API_KEY,
        default_headers = {"X-Groq-JSON-Mode": "true"}
) 

parser = PydanticOutputParser(
            pydantic_object = RAGResponse
)

structured_llm = llm.with_structured_output(RAGResponse)

SYSTEM_PROMPT = """You are a strictly grounded technical assistant.
RULES:
1. Answer ONLY using the provided context. Do not use external knowledge.
2. If the context lacks information, respond EXACTLY with: "I don't have enough information in the provided documents."
3. Cite every claim using exact filenames and sections from the context.
4. Return ONLY valid JSON matching the schema. No markdown, no extra text.

Context:
{context}

Question: {question}"""


prompt = ChatPromptTemplate.from_messages([
            ("system", SYSTEM_PROMPT),
            ("human", "{question}")
])

def format_context(chunks: list[dict] | None) -> str:
    if not chunks:
        return "NO CONTEXT PROVIDED."
    
    lines = []

    for i, c in enumerate(chunks):
        lines.append(f"[Source {i+1}] {c['filename']} | {c['section']}\n{c['page_content']}")

    return "\n---\n".join(lines)


rag_chain = (
    {"context": lambda x: format_context(x.get("chunks")),
     "question": lambda x: x["question"] }
     | prompt | structured_llm 
)

def generate(query:str, chunks: list[dict] | None) -> dict:
    fallback = {"answer": "I don't have enough infromation in the provided documents.", "source": []}
    
    if chunks is None or len(chunks) == 0:
        logger.info("No context provided to LLM.")
        return fallback
    
    try:
        result = rag_chain.invoke({
                    "question": query,
                    "chunks": chunks
        })
        return result.model_dump()

    except ValidationError as e:
        logger.warning(f"Pydentic validation failed: {e}")
        return fallback
    except Exception as e:
        logger.error(f"Generation Error: {e}", exc_info=True)
        return fallback
      