import streamlit as st
import whisper
import tempfile
import os
from dotenv import load_dotenv
from audio_recorder_streamlit import audio_recorder
from rag import run_rag       

load_dotenv()

st.set_page_config(page_title="RAG for LemonTea", page_icon="⚡️")
st.title("Lemon - Multimodel RAG⚡️")
st.write("Upload a file or record audio and you can ask anything about it!")

@st.cache_resource
def load_whisper():
    return whisper.load_model("base")

def transcribe(file_path: str) -> str:
    model = load_whisper()
    result = model.transcribe(file_path)
    return result["text"]

def save_temp_file(data: bytes, suffix: str) -> str:
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as f:
        f.write(data)
        return f.name

st.header("Step 1: Provide Source Content")

tab1, tab2, tab3 = st.tabs(["📄 Upload Text", "🎵 Upload Audio", "🎤 Record Audio"])

source_text = None      

with tab1:
    st.write("Upload a `.txt` file as your knowledge base.")
    txt_file = st.file_uploader("Choose a text file", type=["txt"])
    if txt_file:
        source_text = txt_file.read().decode("utf-8")
        st.success("Text file loaded!")
        st.text_area("Preview", source_text[:300] + "...", height=100, disabled=True)

with tab2:
    st.write("Upload an audio file — it will be transcribed automatically.")
    audio_file = st.file_uploader("Choose an audio file", type=["mp3", "wav", "m4a"])
    if audio_file:
        st.audio(audio_file)  
        with st.spinner("Transcribing audio... this may take a moment"):
            tmp_path = save_temp_file(audio_file.read(), suffix=".mp3")
            source_text = transcribe(tmp_path)
            os.unlink(tmp_path)  
        st.success("Audio transcribed!")
        st.text_area("Transcript Preview", source_text[:300] + "...", height=100, disabled=True)

with tab3:
    st.write("Record directly from your microphone.")
    audio_bytes = audio_recorder()
    if audio_bytes:
        st.audio(audio_bytes, format="audio/wav")
        with st.spinner("Transcribing recording..."):
            tmp_path = save_temp_file(audio_bytes, suffix=".wav")
            source_text = transcribe(tmp_path)
            os.unlink(tmp_path)
        st.success("Recording transcribed!")
        st.text_area("Transcript", source_text[:300] + "...", height=100, disabled=True)

st.header("Step 2: Ask a Question")

if source_text:
    query = st.text_input("Type your question here")

    if st.button("Get Answer") and query:
        with st.spinner("Thinking..."):
            answer = run_rag(source_text, query)

        st.subheader("💬 Answer")
        st.write(answer)
else:
    st.info("Please provide a source document above first.")