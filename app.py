import streamlit as st
import os
from extractor import extract_text_from_resume
from parser import parse_resume

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

st.title("📄 Resume Parser")
st.write("Upload a resume to extract details")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf","docx","png","jpg","jpeg"]
)

if uploaded_file:

    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

    with st.spinner("Extracting text..."):
        text = extract_text_from_resume(file_path)

    with st.spinner("Parsing resume..."):
        parsed = parse_resume(text)

    st.subheader("📊 Extracted Information")

    st.write("### 👤 Name")
    st.write(parsed["name"])

    st.write("### 📧 Email")
    st.write(parsed["email"])

    st.write("### 📱 Phone")
    st.write(parsed["phone"])

    st.write("### 🧠 Skills")
    st.write(parsed["skills"])

    st.write("### 🎓 Education")
    st.write(parsed["education"])

    st.write("### 💼 Experience")
    st.write(parsed["experience"])

    st.write("### 🔍 Raw Extracted Text")
    st.text_area("Resume Text", text, height=300)