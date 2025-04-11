import docx2txt
import PyPDF2
from io import BytesIO

def extract_text_from_file(uploaded_file):
    try:
        file_type = uploaded_file.name.split('.')[-1].lower()

        if file_type == "pdf":
            reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""  # Handle None returns
            return text.strip()

        elif file_type == "docx":
            uploaded_file.seek(0)  # Ensure pointer is at the start
            return docx2txt.process(BytesIO(uploaded_file.read())).strip()

        else:
            return "Unsupported file format. Please upload a PDF or DOCX."

    except Exception as e:
        return f"Error extracting text: {str(e)}"
