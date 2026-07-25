# DocuMind AI 🤖

An AI-powered document assistant built using Retrieval-Augmented Generation (RAG).  
DocuMind AI allows users to interact with PDF documents by retrieving relevant information from documents and generating intelligent responses using a local Large Language Model.

---

# 🚀 Features

- PDF document processing
- Automatic text extraction and chunking
- Semantic search using embeddings
- Vector storage using ChromaDB
- Retrieval-Augmented Generation pipeline
- Local AI responses using Ollama
- Conversation-based question answering
- FastAPI backend support
- Modular AI architecture

---

# 🏗️ Architecture
            PDF Document
                 |
                 v
        PDF Processor
                 |
                 v
          Text Chunks
                 |
                 v
      Embedding Generation
      (Nomic Embed Text)
                 |
                 v
          ChromaDB
      Vector Database
                 |
                 v
      Relevant Context Retrieval
                 |
                 v
           Qwen LLM
                 |
                 v
            AI Answer
---

# 🛠️ Tech Stack

## Programming Language
- Python

## AI / Machine Learning
- Ollama
- Qwen2.5 LLM
- Nomic Embed Text

## Backend
- FastAPI
- Uvicorn

## Database
- ChromaDB

## Document Processing
- PyPDF

---

# 📂 Project Structure
DocuMind-AI/

│
├── app.py # Terminal based application
├── api.py # FastAPI backend
├── rag_engine.py # Main RAG pipeline controller
│
├── pdf_processor.py # PDF extraction and chunking
├── embeddings.py # Text embedding generation
├── database.py # ChromaDB operations
├── llm.py # LLM response generation
│
├── Data/ # Add PDF documents here
│
├── requirements.txt
├── README.md
└── .gitignore
---

# ⚙️ Installation

Clone the repository:

```bash
Install dependencies:
git clone <repository-url>
pip install -r requirements.txt

🧠 Required Ollama Models

Install Ollama from:

https://ollama.com

Pull the embedding model:

ollama pull nomic-embed-text

Pull the language model:

ollama pull qwen2.5:1.5b
▶️ Running the Application
Terminal Version

Run:

python app.py

The application will allow you to select a PDF document and ask questions about its content.

API Version

Start FastAPI:

uvicorn api:app --reload

Open:

http://127.0.0.1:8000/docs