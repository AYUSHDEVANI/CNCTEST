import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Set the base path  or directory and set raw directopry for raw data 
BASE_DIR = Path(__file__).parent.parent.resolve()
RAW_DIR = BASE_DIR / "data" / "raw"
MODEL_DIR = BASE_DIR / "vector_db"
MODEL_DIR.mkdir(exist_ok=True)


MAX_CHUNK_TOKENS = 256   #mention in the documenet - max chunk token after spillting = 256
CONTEXT_MAX_TOKENS = 3000  #max window size
RETRIEVE_TOP_K = 10         # Get the top 10 most similar chunks from the vector store
SCORE_THRESHOLD = 0.35      #set the threshold for checking similarity

# Embedding model
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# Groq model and api key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.3-70b-versatile"


