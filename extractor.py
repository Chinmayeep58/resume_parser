import os
from pdfminer.high_level import extract_text
from docx import Document
import pytesseract
import cv2
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\CHINMAYEE\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])


def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return pytesseract.image_to_string(gray)


def extract_text_from_pdf_file(pdf_path):
    try:
        text = extract_text(pdf_path)
        if text.strip():
            return text
    except:
        pass

    images = convert_from_path(pdf_path)
    text = ""

    for img in images:
        text += pytesseract.image_to_string(img)

    return text


def extract_text_from_resume(file_path):

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return extract_text_from_pdf_file(file_path)

    elif ext == ".docx":
        return extract_text_from_docx(file_path)

    elif ext in [".png", ".jpg", ".jpeg"]:
        return extract_text_from_image(file_path)

    else:
        raise ValueError("Unsupported file format")