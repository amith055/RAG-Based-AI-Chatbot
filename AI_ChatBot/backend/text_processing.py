from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextProcessing:
    def __init__(self):
        pass

    @staticmethod
    def extract_text(filename):
        reader = PdfReader(filename)
        text = ""
        for page in reader.pages:
            text+= page.extract_text() + '\n'
        return text
    
    @staticmethod
    def getchunks(content):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size = 400,
            chunk_overlap = 100
        )
        chunks = splitter.split_text(content)

