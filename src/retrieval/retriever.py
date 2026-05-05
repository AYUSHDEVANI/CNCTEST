import tiktoken
import numpy as np
import logging
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from src.config import MODEL_DIR, RETRIEVE_TOP_K, SCORE_THRESHOLD, CONTEXT_MAX_TOKENS, EMBEDDING_MODEL_NAME

ENCODER = tiktoken.get_encoding("cl100k_base")
logger = logging.getLogger(__name__)

def build_retriever():

    try:


        embeddings = HuggingFaceEmbeddings(
                    model_name = EMBEDDING_MODEL_NAME,
                    model_kwargs = {"device": "cpu"}
        )

        vectorstore = FAISS.load_local(
            str(MODEL_DIR.resolve()), 
            embeddings=embeddings,
            allow_dangerous_deserialization=True
            )
        
        index = vectorstore.index
        index_to_docstore = vectorstore.docstore._dict

    except Exception as e:
        logger.error(f"Failed to load vectore store: {e}")
        raise RuntimeError("Vectore stire not initialized.")

    def query(query_text: str):
        try:
            q_vec = embeddings.embed_query(query_text)
            q_vec = np.array(q_vec, dtype="float32").reshape(1, -1)
            norm = np.linalg.norm(q_vec)
            if norm == 0:
                logger.warning("Zero norm query embedding")
                return None
            # q_vec = q_vec / norm


            scores, idxs = index.search(q_vec, RETRIEVE_TOP_K)
            scores, idxs = scores[0], idxs[0]

            print("Scores:", scores)

            # if len(scores) == 0 or min(scores) > SCORE_THRESHOLD:
            #     logger.info(f"Query below threshold (min_score={min(scores) if len(scores)>0 else 'N/A'})")
            #     return None

            seen = set()
            candidates = []
            for s, i in zip(scores, idxs):
                if i == -1:
                    continue

                doc = index_to_docstore.get(str(i))
                if not doc or not hasattr(doc, "page_content") or not doc.page_content:
                    continue
                if doc.page_content in seen:
                    continue

                metadata = getattr(doc, 'metadata', {}) or {}
                filename = metadata.get('filename', 'unknown.md')
                section = metadata.get('section', 'Root')

                seen.add(doc.page_content)
                candidates.append({
                    "page_content": doc.page_content,
                    "filename": filename,
                    "section": section,
                    "similarity_score": float(s)
                })

            if not candidates:
                logger.warning("No valid candidates after retrival")
                return None

            
            context_chunks = []
            total_tok = 0

            for c in candidates:
                t_len = len(ENCODER.encode(c["page_content"]))

                if total_tok + t_len > CONTEXT_MAX_TOKENS:
                    break

                context_chunks.append(c)
                total_tok += t_len

            logger.info(f"Retrived {len(context_chunks)} chunks for query")
            return context_chunks
        
        except Exception as e:
            logger.error(f"Retrieval error: {e}, exc_info=True")
            return None
    
    return query
        