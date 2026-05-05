import tiktoken
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from src.config import RAW_DIR, MAX_CHUNK_TOKENS


ENCODER = tiktoken.get_encoding("cl100k_base")


def load_and_chunk() -> list[Document]:
    raw_docs = []
    for fp in RAW_DIR.glob("*.md"):
        raw_docs.append(Document(page_content=fp.read_text(encoding="utf-8"), metadata = {"filename": fp.name}))


    # Split heading and normal text based on the header
    header_splitter = MarkdownHeaderTextSplitter(
                        headers_to_split_on = [("#", "h1"), ("##", "h2"), ("###", "h3")]
    )

    header_docs = []
    for doc in raw_docs:
            # split_text returns a list of Document objects with header metadata
            splits = header_splitter.split_text(doc.page_content)
            
            # Manually add your custom 'filename' metadata back into each split
            for split in splits:
                split.metadata.update(doc.metadata)
                header_docs.append(split)

    for doc in header_docs:
        parts = [doc.metadata.get(h, "") for h in ("h1", "h2", "h3") if doc.metadata.get(h)]
        doc.metadata["section"] = " > ".join(parts) or "Root"
        for h in ("h1", "h2", "h3"):
            doc.metadata.pop(h, None)


    token_splitter = RecursiveCharacterTextSplitter(
        chunk_size = MAX_CHUNK_TOKENS,
        chunk_overlap = 30,
        length_function = lambda t: len(ENCODER.encode(t))
    )

    chunks = token_splitter.split_documents(header_docs)


    for c in chunks:
        c.metadata["token_count"] = len(ENCODER.encode(c.page_content))

    return chunks
    