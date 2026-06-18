import docx2txt
from PyPDF2 import PdfReader

def extract_text_from_file(uploaded_file):
    """
    Extracts text from different file types.
    :param uploaded_file: Uploaded file object
    :return: Extracted text as a string
    """
    if uploaded_file.type == "text/plain":
        return uploaded_file.read().decode("utf-8")
    elif uploaded_file.type == "application/pdf":
        text = ""
        pdf_reader = PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return docx2txt.process(uploaded_file)
    return ""