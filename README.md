# Resume Parser & Analysis System

**Last Updated:** March 2026

## Overview

This project implements a **Resume Parsing and Analysis System** capable of extracting structured information from resumes in multiple formats. The system automatically processes resumes and extracts important details such as **name, email, phone number, skills, education, and experience**.

The parser supports multiple input formats including:

* PDF resumes
* DOCX resumes
* Image-based resumes (JPG, PNG, JPEG)

The goal of this project is to demonstrate how **Natural Language Processing (NLP), OCR, and rule-based extraction** can be combined to automatically structure unformatted resume data.

This repository is designed for **learning, experimentation, and extension**, especially for projects related to **ATS systems, recruitment automation, and resume analytics**.

---

## Generic Resume Parsing Architecture

A typical resume parsing system follows the pipeline below:

Resume Input → Text Extraction → Text Cleaning & Preprocessing → Information Extraction → Structured Output → Feedback & Improvement

Core components:

1. Resume Input (PDF / DOCX / Image)
2. Text Extraction (PDF parsing / OCR)
3. Text Cleaning and Normalization
4. NLP-based Entity Extraction
5. Structured Resume Output
6. Feedback Loop for improving extraction accuracy

---

## System Workflow

### Resume Upload

Users upload resumes through the **Streamlit frontend interface**.

Supported formats:

* `.pdf`
* `.docx`
* `.png`
* `.jpg`
* `.jpeg`

---

### Text Extraction

Different extraction pipelines are used depending on the resume format.

PDF resumes
→ Extracted using **pdfminer**

DOCX resumes
→ Extracted using **python-docx**

Image-based resumes
→ Extracted using **Tesseract OCR**

This ensures the system can handle both **digital resumes and scanned resumes**.

---

### Text Preprocessing

The extracted text is cleaned and normalized to improve extraction accuracy.

Operations include:

* Removing unnecessary whitespace
* Normalizing line breaks
* Preparing text for NLP processing

---

### Information Extraction

The system extracts key resume information:

**Personal Information**

* Name (using SpaCy Named Entity Recognition)
* Email address (regex)
* Phone number (regex)

**Skills**

Detected using a predefined skill set including examples such as:

* Python
* SQL
* Excel
* Power BI
* Machine Learning
* Data Science

**Education**

Lines containing education-related keywords such as:

* Bachelor
* Master
* B.Sc
* M.Sc
* PhD
* B.E
* M.E

**Experience**

Sections containing keywords like:

* Experience
* Work
* Internship
* Employment

---

### Structured Resume Output

The extracted information is returned as a structured dictionary:

Example output:

```
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+91 9876543210",
  "skills": ["Python", "SQL", "Machine Learning"],
  "education": ["Bachelor of Technology in Computer Science"],
  "experience": ["Software Intern at ABC Company"]
}
```

This structured output can be used in:

* Applicant Tracking Systems (ATS)
* Candidate ranking systems
* Job recommendation engines
* HR automation tools

---

## Feedback Loop & Quality Improvement

To improve the quality of extracted results, the system can incorporate a **feedback loop**.

Examples of feedback signals:

* User correction of extracted fields
* Validation of extracted skills
* Manual review by recruiters

This feedback can be used to:

* Improve skill detection
* Refine regex patterns
* Train improved NLP models

Over time this leads to **more accurate resume parsing**.

---

## Repository Structure

```
resume-parser/
│
├── app.py                # Streamlit frontend interface
├── extractor.py          # Resume text extraction logic
├── parser.py             # Resume information extraction
│
├── uploads/              # Uploaded resume files
│
├── tests/                # Unit tests
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/<your-username>/resume-parser.git
cd resume-parser
```

Create a virtual environment:

```
python -m venv venv
```

Activate the environment:

Windows

```
venv\Scripts\activate
```

Linux / Mac

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Install SpaCy language model:

```
python -m spacy download en_core_web_sm
```

Install Tesseract OCR (required for image-based resumes):

https://github.com/UB-Mannheim/tesseract/wiki

---

## Running the Application

Run the Streamlit application:

```
streamlit run app.py
```

The application will launch at:

```
http://localhost:8501
```

Users can upload resumes and view the extracted results through the web interface.

---

## Data Sources

This project **does not include resume datasets** in the repository.

Users interested in experimentation can explore publicly available datasets such as:

Resume datasets

* Kaggle Resume Dataset
  https://www.kaggle.com

Job description datasets

* Kaggle Job Postings Dataset
  https://www.kaggle.com

These datasets can be used to test and extend the parser.

---

## Code Quality & Documentation

The codebase follows good software engineering practices:

* Clear function naming
* Modular architecture
* Inline documentation
* Separation of extraction and parsing logic

Recommended additions:

* Unit tests for parsing functions
* Additional logging for debugging
* Improved NLP-based entity extraction

Unit tests can be run using:

```
pytest
```

---

## Future Enhancements

Possible extensions for this project include:

* Advanced NLP-based skill extraction
* Resume scoring against job descriptions
* Candidate ranking system
* Automatic skill gap detection
* Job recommendation system
* Resume quality scoring
* Deep learning-based NER models
* ATS compatibility analysis
* Resume summarization using LLMs

These enhancements can transform the system into a **complete AI-powered recruitment assistant**.

---

## Collaboration

This repository is open for collaboration.

Contributors are welcome to:

* Submit pull requests
* Suggest improvements
* Add new features
* Improve extraction accuracy

You are also encouraged to **fork the repository and build new applications on top of this system**.

---

## References

Useful resources for deeper understanding:

SpaCy NLP Documentation
https://spacy.io

Tesseract OCR Documentation
https://tesseract-ocr.github.io

PDFMiner Documentation
https://pdfminersix.readthedocs.io

Streamlit Documentation
https://streamlit.io

---


Feel free to open an issue for questions, improvements, or collaboration.
