from src.ingestion.chunker import load_and_chunk
from src.vector.faiss_store import save_vectorstore

print("Loading.....")
chunks = load_and_chunk()
print(f"Successfully generated: {len(chunks)} chunks")


save_vectorstore(chunks)
print("Successfully stored vector store.")