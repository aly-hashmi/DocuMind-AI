from pathlib import Path
from pypdf import PdfReader


class PDFDocument:

    def __init__(self, filename):
        self.filename = filename
        self.text = ""

    def load(self):

        current_folder = Path(__file__).parent
        data_folder = current_folder / "data"
        file_path = data_folder / self.filename

        reader = PdfReader(file_path)

        for page in reader.pages:
            self.text += page.extract_text()


    def chunk_text(self):

        chunk_size = 500
        overlap = 100

        chunks = []

        start = 0

        while start < len(self.text):

            end = start + chunk_size

            chunks.append(self.text[start:end])

            start += chunk_size - overlap

        return chunks
    from pathlib import Path


def list_pdfs():

    current_folder = Path(__file__).parent

    data_folder = current_folder / "data"

    pdf_files = []

    for file in data_folder.iterdir():

        if file.suffix.lower() == ".pdf":

            pdf_files.append(file.name)

    return pdf_files