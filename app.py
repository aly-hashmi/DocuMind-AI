from pdf_processor import PDFDocument, list_pdfs
from embeddings import create_embedding
from database import VectorDatabase
from llm import ask_llm


# -----------------------------
# PDF Selection
# -----------------------------

print("\n===================================")
print("        PDF RAG Assistant")
print("===================================\n")

pdfs = list_pdfs()

if len(pdfs) == 0:
    print("No PDF files found inside the data folder.")
    exit()

print("Available PDFs:\n")

for index, pdf in enumerate(pdfs, start=1):
    print(f"{index}. {pdf}")

while True:

    try:

        choice = int(input("\nChoose a PDF by number: "))

        if 1 <= choice <= len(pdfs):
            break

        print("Please enter a valid number.")

    except ValueError:

        print("Please enter numbers only.")

filename = pdfs[choice - 1]

print(f"\nSelected PDF: {filename}")


# -----------------------------
# Load PDF
# -----------------------------

pdf = PDFDocument(filename)
pdf.load()
chunks = pdf.chunk_text()


# -----------------------------
# Database
# -----------------------------

db = VectorDatabase()

if db.pdf_exists(filename):

    print("\nPDF already indexed.")

else:

    print("\nIndexing PDF...")

    db.add_pdf(filename, chunks)

    print("Indexing complete.")


# -----------------------------
# Conversation Memory
# -----------------------------

conversation_history = []


# -----------------------------
# Chat Loop
# -----------------------------

while True:

    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        print("Chat ended.")
        break

    # Create embedding of the user's question
    question_embedding = create_embedding(question)

    # Retrieve the most relevant chunks
    best_chunks = db.search(
        question_embedding,
        filename
    )

    # Merge retrieved chunks into one context
    context = "\n\n".join(best_chunks)

    # Ask the LLM
    answer = ask_llm(
        question,
        context,
        conversation_history
    )

    # Save conversation history
    conversation_history.append(
        {
            "role": "user",
            "content": question
        }
    )

    conversation_history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # Print answer
    print("\nAnswer:\n")
    print(answer)