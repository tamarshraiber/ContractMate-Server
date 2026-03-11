# חילוץ טקסט מ-PDF / Word

import pdfplumber
from docx import Document


def extract_text_from_pdf(file_path):
    """
    הפונקציה מקבלת נתיב של PDF
    ומחזירה את כל הטקסט שנמצא במסמך
    """

    text = ""

    # פתיחת ה-PDF
    with pdfplumber.open(file_path) as pdf:

        # מעבר על כל העמודים
        for page in pdf.pages:

            # חילוץ טקסט מכל עמוד
            page_text = page.extract_text()

            # אם נמצא טקסט – להוסיף אותו
            if page_text:
                text += page_text + "\n"

    return text


def extract_text_from_docx(file_path):
    """
    חילוץ טקסט מקובץ Word
    """

    doc = Document(file_path)

    text = ""

    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"

    return text