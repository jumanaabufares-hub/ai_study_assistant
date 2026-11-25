# 📖 AI Study Assistant

AI Study Assistant is a Python chatbot that helps students understand and review their lecture notes. Users can upload PDF files, ask questions, and receive AI-generated summaries and explanations using Google's Gemini API.

## Features

- Upload PDF lecture notes.
- Ask questions based on uploaded documents.
- Summarize lecture notes.
- Explain concepts in simple terms with examples.
- Display responses through a Streamlit chatbot interface.

## Technologies Used

- **Python**: Main programming language
- **Streamlit**: Web interface
- **Google Gemini API**: AI-generated responses
- **PyMuPDF**: Extract text from PDF files
- **python-dotenv**: Manage API key configuration

## Project Structure

```text
ai_study_assistant/
├── app.py
├── check.py
├── requirements.txt
├── .env
└── README.md
```

- `app.py` — Main application for uploading PDFs, asking questions, and generating AI responses.
- `check.py` — Checks available Gemini models that support content generation.
- `requirements.txt` — Lists the Python libraries required for the project.
- `.env` — Stores the Gemini API key locally and should not be uploaded to GitHub.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/USERNAME/ai_study_assistant.git
cd ai_study_assistant
```

### 2. Install dependencies

Make sure Python is installed, then run:

```bash
python -m pip install -r requirements.txt
```

### 3. Set up Gemini API

1. Go to Google AI Studio.
2. Create an API key.
3. Create a `.env` file in the project folder.
4. Add the following:

```env
GEMINI_API_KEY=created_api_key
```

Replace the placeholder with your API key.

### 4. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

### 5. Check available models (optional)

```bash
python check.py
```

This displays Gemini models that support generating content.

## How to Use

1. Upload a PDF containing lecture notes.
2. Type a question or request a summary.
3. The chatbot extracts text from the PDF.
4. Gemini generates a response based on the uploaded material.

Example questions:

- Summarize these notes.
- Explain relational algebra in simple terms.
- What are the main concepts in this lecture?
- Give me an example of a B+ Tree.

## Current Limitations

- Supports one PDF at a time.
- Processes up to 30,000 characters of extracted PDF text.
- Does not support scanned PDFs without extractable text.
- AI responses may contain inaccuracies.
- Conversations are not permanently stored.

## Future Improvements

- Add conversation history.
- Support multiple PDF uploads.
- Implement RAG and semantic search.
- Add source references.
- Test and evaluate response accuracy and reliability.

## Project Status

**In Progress: November 2026**

This project is being developed to gain practical experience with Python, large language models, API integration, and AI application development.
