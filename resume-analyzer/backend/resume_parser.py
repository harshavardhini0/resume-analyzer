import PyPDF2
import re
from docx import Document

skills_db = [
    "python", "java", "c++", "html", "css", "javascript",
    "sql", "machine learning", "data science", "react"
]

def extract_text(file_path):
    try:
        if file_path.endswith(".pdf"):
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    if page.extract_text():
                        text += page.extract_text()

        elif file_path.endswith(".txt"):
            with open(file_path, 'r', encoding="utf-8") as file:
                text = file.read()

        elif file_path.endswith(".docx"):
            doc = Document(file_path)
            text = ""
            for para in doc.paragraphs:
                text += para.text

        else:
            return "unsupported"

        return text.lower()

    except:
        return "error"


def extract_skills(text):
    found_skills = []
    for skill in skills_db:
        if re.search(r'\b' + re.escape(skill) + r'\b', text):
            found_skills.append(skill)
    return found_skills