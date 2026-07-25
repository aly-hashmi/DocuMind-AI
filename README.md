# 🧠 DocuMind AI

> An AI-powered PDF Question Answering System built using **Retrieval-Augmented Generation (RAG)**, **ChromaDB**, **Ollama**, and **FastAPI**.

DocuMind AI allows users to upload PDF documents, index them into a vector database, and ask natural language questions. The system retrieves the most relevant document context using semantic search and generates accurate responses using a local Large Language Model (LLM).

---

# 📸 Demo

## Terminal Application

![Terminal Demo](assets/terminal.PNG)

---

## FastAPI Swagger UI

![FastAPI Swagger UI](assets/fastAPI.PNG)

---

# ✨ Features

- 📄 PDF text extraction
- ✂️ Automatic text chunking
- 🧠 Semantic embeddings using Nomic Embed
- 🗂️ Vector storage with ChromaDB
- 🔍 Similarity search for relevant context
- 🤖 AI-generated answers using Qwen (Ollama)
- 💬 Multi-turn conversational memory
- 🌐 REST API built with FastAPI
- 🖥️ Terminal-based chatbot interface
- 📚 Supports indexing multiple PDF documents

---

# 🏗️ System Architecture

```text
                PDF Document
                     │
                     ▼
           PDF Text Extraction
                     │
                     ▼
              Text Chunking
                     │
                     ▼
          Nomic Embed Text Model
                     │
                     ▼
            ChromaDB Vector Store
                     │
                     ▼
         Semantic Similarity Search
                     │
                     ▼
            Retrieved PDF Context
                     │
                     ▼
           Qwen LLM (via Ollama)
                     │
                     ▼
              AI Generated Answer
```

---

# ⚙️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| LLM | Qwen 2.5 (Ollama) |
| Embedding Model | Nomic Embed Text |
| Vector Database | ChromaDB |
| Backend | FastAPI |
| API Server | Uvicorn |
| PDF Processing | PyPDF |
| Similarity Search | Scikit-learn (Cosine Similarity) |

---

# 📂 Project Structure

```text
DocuMind-AI/

├── api.py                 # FastAPI backend
├── app.py                 # Terminal chatbot
├── rag_engine.py          # RAG workflow
├── database.py            # ChromaDB operations
├── embeddings.py          # Embedding generation
├── llm.py                 # Ollama LLM interaction
├── pdf_processor.py       # PDF loading & chunking
│
├── Data/
│
├── assets/
│   ├── terminal.PNG
│   └── fastAPI.PNG
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🚀 How It Works

1. Select a PDF document.
2. Extract text from the PDF.
3. Split the document into manageable chunks.
4. Generate embeddings for each chunk.
5. Store embeddings inside ChromaDB.
6. Convert the user's question into an embedding.
7. Retrieve the most relevant chunks using semantic search.
8. Send the retrieved context and question to the LLM.
9. Generate an accurate answer grounded in the document.

---

# 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/aly-hashmi/DocuMind-AI.git
cd DocuMind-AI
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

# 🤖 Install Required Ollama Models

Pull the embedding model:

```bash
ollama pull nomic-embed-text
```

Pull the language model:

```bash
ollama pull qwen2.5:1.5b
```

Ensure the Ollama service is running before starting the application.

---

# ▶️ Running the Application

### Terminal Version

```bash
python app.py
```

The application allows you to:

- Select a PDF document
- Ask questions about its contents
- Receive AI-generated responses grounded in the document

---

### FastAPI Backend

Start the server:

```bash
uvicorn api:app --reload
```

Open the interactive API documentation:

```
http://127.0.0.1:8000/docs
```

---

# 💡 Example Questions

- What is Machine Learning?
- Summarize Chapter 3.
- Explain supervised learning.
- List the key concepts discussed.
- What are the advantages of AI?

---

# 📈 Future Improvements

- Web frontend (React/Next.js)
- Drag-and-drop PDF uploads
- Multi-document chat sessions
- User authentication
- Persistent chat history
- Hybrid search (keyword + semantic)
- Streaming LLM responses
- Cloud deployment (Docker/AWS)

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Semantic Search
- Vector Databases
- FastAPI Development
- REST API Design
- Local AI Deployment
- Document Intelligence

---

# 👨‍💻 Author

**Aly Hashmi**

Computer Science Student | AI & Python Enthusiast

GitHub: https://github.com/aly-hashmi

---

## ⭐ If you found this project interesting, consider giving it a star!
