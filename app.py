import os
import pymupdf 
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="AI Study Assistant", page_icon="📖")

st.title("📖 AI Study Assistant")
st.write("Upload your lecture notes and ask questions!")

# keep previous messages
if "messages" not in st.session_state:
    st.session_state.messages = []

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

pdf_text = ""

# get the text from the PDF using fitz
if uploaded_file:
    with pymupdf.open(stream=uploaded_file.getvalue(), filetype="pdf") as pdf:
        for page in pdf:
            pdf_text += page.get_text()

    st.success(f"{uploaded_file.name} uploaded successfully.")

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask AI Study Assistant...")


if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        if not api_key:
            st.error("API key is missing")

        elif not pdf_text.strip():
            st.warning("Upload a PDF file first")

        else:
            try:
                with st.spinner("Thinking..."):
                    client = genai.Client(api_key=api_key)
                    # ask gemini using PDF
                    response = client.models.generate_content(
                        model="gemini-3.5-flash-lite",
                        contents=f"Notes:\n{pdf_text[:30000]}\n\nQuestion: {question}",
                        config=types.GenerateContentConfig(
                            system_instruction=(
                                "Answer based on the notes. "
                                "Summarize when asked and explain things clearly. "
                                "Keep answers simple and use examples if needed. "
                                "If something isn't in the notes, say so."
                            )
                        )
                    )

                answer = response.text or "No answer"
                st.write(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:
                st.error(f"Error: {e}")
