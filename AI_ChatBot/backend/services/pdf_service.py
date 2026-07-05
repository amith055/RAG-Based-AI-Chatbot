from pypdf import PdfReader

def extract_text(filename):
    reader = PdfReader(filename)
    text = ""
    for page in reader.pages:
        text+= page.extract_text() + "\n"
    return text