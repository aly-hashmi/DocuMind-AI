import chromadb

from embeddings import create_embedding


class VectorDatabase:

    def __init__(self):

        self.client = chromadb.PersistentClient(path="./chroma_db")

        self.collection = self.client.get_or_create_collection(
            name="pdf_chunks"
        )

    def pdf_exists(self, filename):

        results = self.collection.get(
            where={"source": filename}
        )

        return len(results["ids"]) > 0

    def add_pdf(self, filename, chunks):

        for index, chunk in enumerate(chunks):

            embedding = create_embedding(chunk)

            self.collection.add(

                ids=[f"{filename}_{index}"],

                documents=[chunk],

                embeddings=[embedding],

                metadatas=[

                    {
                        "source": filename,
                        "chunk": index
                    }

                ]

            )

    def search(self, question_embedding, filename):

        results = self.collection.query(

            query_embeddings=[question_embedding],

            n_results=3,

            where={"source": filename}

        )

        return results["documents"][0]