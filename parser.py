import re
import spacy

nlp = spacy.load("en_core_web_sm")

skill_set = [
    'python','sql','excel','power bi',
    'machine learning','data science'
]

education_keywords = [
    'bachelor','master','b.sc','m.sc','phd','b.e','m.e'
]


def clean_text(text):
    text = re.sub(r'\n+','\n',text)
    text = re.sub(r' +',' ',text)
    return text.strip()


def extract_email(text):
    match = re.search(r'\S+@\S+', text)
    return match.group(0) if match else None


def extract_phone(text):
    match = re.search(r'\+?\d[\d\s\-\(\)]{8,15}', text)
    return match.group(0) if match else None


def extract_name(text):
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return None


def extract_skills(text):

    found = [skill for skill in skill_set if skill.lower() in text.lower()]
    return list(set(found))


def extract_education(text):

    education = []
    lines = text.split('\n')

    for line in lines:
        for word in education_keywords:
            if word in line.lower():
                education.append(line.strip())

    return education


def extract_experience(text):

    keywords = ['experience','work','internship','employment']
    exp = []

    lines = text.split('\n')

    for line in lines:
        for word in keywords:
            if word in line.lower():
                exp.append(line.strip())

    return exp


def parse_resume(text):

    text = clean_text(text)

    parsed = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "education": extract_education(text),
        "experience": extract_experience(text)
    }

    return parsed