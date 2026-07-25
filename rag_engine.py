from pdf_processor import PDFDocument, list_pdfs
from embeddings import create_embedding
from database import VectorDatabase
from llm import ask_llm


class RAGEngine:

    def __init__(self, filename):

        self.filename = filename

        self.pdf = PDFDocument(filename)

        self.pdf.load()

        self.chunks = self.pdf.chunk_text()

        self.db = VectorDatabase()


        # Check if PDF is already stored

        if self.db.pdf_exists(filename):

            print("PDF already indexed.")

        else:

            print("Indexing PDF...")

            self.db.add_pdf(
                filename,
                self.chunks
            )

            print("Indexing complete.")


        # Conversation memory

        self.conversation_history = []


    def ask(self, question):

        # Create question embedding

        question_embedding = create_embedding(question)


        # Retrieve relevant chunks

        best_chunks = self.db.search(
            question_embedding,
            self.filename
        )


        context = "\n\n".join(best_chunks)


        # Ask LLM

        answer = ask_llm(
            question,
            context,
            self.conversation_history
        )


        # Save conversation

        self.conversation_history.append(
            {
                "role": "user",
                "content": question
            }
        )


        self.conversation_history.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


        return answer