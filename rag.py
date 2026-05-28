import os
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
import streamlit as st

load_dotenv()

@st.cache_resource
def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

def run_rag(text: str, query: str) -> str:
    documents = [Document(page_content=text)]
    text_splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    docs = text_splitter.split_documents(documents)

    embeddings = get_embeddings()

    db = FAISS.from_documents(docs, embeddings)
    retrieved_docs = db.similarity_search(query, k=3)
    
    context = "\n".join([doc.page_content for doc in retrieved_docs])

    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    prompt = f"""
    Answer ONLY from the context below:

    {context}

    Question: {query}
    """

    response = llm.invoke(prompt)
    return response.content