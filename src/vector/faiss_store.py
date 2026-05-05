import numpy as np
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from src.config import EMBEDDING_MODEL_NAME, MODEL_DIR

embedding_model = HuggingFaceEmbeddings(
                    model_name = EMBEDDING_MODEL_NAME,
                    model_kwargs = {"device": "cpu"}
                )

def save_vectorstore(chunks: list):
    vectorstore = FAISS.from_documents(chunks, embedding=embedding_model)
    vectorstore.save_local(str(MODEL_DIR))

    print(f"Store {len(chunks)} chunks to {MODEL_DIR}")

    return vectorstore