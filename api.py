from fastapi import FastAPI
from pydantic import BaseModel
from rag_engine import RAGEngine


app = FastAPI()


# -----------------------------
# Load RAG System
# -----------------------------

rag = RAGEngine("CL.pdf")



class Question(BaseModel):

    question: str



@app.get("/")
def home():

    return {
        "message": "Welcome to my RAG API!"
    }



@app.post("/ask")
def ask_question(data: Question):

    answer = rag.ask(
        data.question
    )


    return {

        "question": data.question,

        "answer": answer

    }