# scripts/ingest.py
import logging
import sys
from pathlib import Path
from src.config import RAW_DIR, MODEL_DIR
from src.ingestion.chunker import load_and_chunk
from src.vector.faiss_store import save_vectorstore

# Configure logging to console + file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("ingest.log", mode="w", encoding="utf-8")
    ]
)
logger = logging.getLogger(__name__)

def main():
    try:
        logger.info(f"🚀 Starting ingestion")
        logger.info(f"📁 Reading from: {RAW_DIR}")
        logger.info(f"💾 Saving to: {MODEL_DIR}")
        
        # Check raw files
        md_files = list(RAW_DIR.glob("*.md"))
        logger.info(f"📄 Found {len(md_files)} .md files: {[f.name for f in md_files]}")
        
        if not md_files:
            raise FileNotFoundError(f"No .md files found in {RAW_DIR}")
        
        # Load & chunk
        logger.info("✂️ Loading and chunking documents...")
        chunks = load_and_chunk()
        logger.info(f"✅ Generated {len(chunks)} chunks")
        
        if not chunks:
            raise ValueError("Chunker returned empty list — check your splitter logic")
        
        # Show sample
        logger.info("📋 Sample chunk:")
        sample = chunks[0]
        logger.info(f"   File: {sample.metadata.get('filename')}")
        logger.info(f"   Section: {sample.metadata.get('section')}")
        logger.info(f"   Tokens: {sample.metadata.get('token_count')}")
        logger.info(f"   Preview: {sample.page_content[:150]}...")
        
        # Save vectorstore
        logger.info("🧠 Building FAISS index...")
        MODEL_DIR.mkdir(parents=True, exist_ok=True)
        save_vectorstore(chunks)
        
        # Verify output
        index_file = MODEL_DIR / "faiss.index"
        meta_file = MODEL_DIR / "metadata.json"
        logger.info(f"✅ Index saved: {index_file.exists()} ({index_file.stat().st_size} bytes)")
        logger.info(f"✅ Metadata saved: {meta_file.exists()} ({meta_file.stat().st_size} bytes)")
        logger.info("🎉 Ingestion complete! Start API with: uvicorn src.api.main:app --reload")
        
    except Exception as e:
        logger.error(f"❌ Ingestion failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()