import streamlit as st
import whisper
import tempfile
import os
from dotenv import load_dotenv
from audio_recorder_streamlit import audio_recorder
from rag import run_rag       

load_dotenv()

st.set_page_config(page_title="RAG for LemonTea", page_icon="⚡️")
st.title("Lemon - Multimodel RAG")
st.write("Upload a file or record audio and you can ask anything about it!")