# Resume Parser -- Concepts Guide

This document explains the **core concepts required to understand the
resume parser code**, including Regex, NLP, PDF processing, and text
processing.

------------------------------------------------------------------------

# 1. PDF Text Extraction

## What is a PDF?

A PDF (Portable Document Format) stores text as **positioned graphical
elements**, not plain text like `.txt` files.

Computers cannot directly read it as normal text.

## Solution: PDF parsing libraries

We use:

``` python
from pdfminer.high_level import extract_text
```

**pdfminer.six** reads the internal structure and reconstructs text.

Concept learned: - File parsing - Document processing

------------------------------------------------------------------------

# 2. Text Preprocessing

Raw extracted text contains:

-   extra spaces
-   extra newlines
-   formatting noise

We clean it using Regex.

Concepts involved:

-   String processing
-   Data cleaning
-   Preprocessing pipeline

Why important: Clean data improves extraction accuracy.

------------------------------------------------------------------------

# 3. Regular Expressions (Regex)

Regex is a **pattern matching language** used to search text.

Python library:

``` python
import re
```

## Example

Email pattern:

``` python
\S+@\S+
```

Meaning:

  Symbol       Meaning
  ------------ ---------------------
  `\S`{=tex}   non‑space character
  \+           one or more
  @            literal @ symbol

Matches:

example@gmail.com

------------------------------------------------------------------------

## Phone regex example

``` python
\+?\d[\d\s\-\(\)]{8,15}
```

Concepts:

  Symbol               Meaning
  -------------------- --------------------
  +?                   optional plus
  `\d |`{=tex} digit   
  \[\]                 allowed characters
  {8,15}               length range

Regex is widely used in:

-   resume parsing
-   validation
-   web scraping

------------------------------------------------------------------------

# 4. Natural Language Processing (NLP)

NLP allows computers to understand human language.

Library used:

``` python
import spacy
```

------------------------------------------------------------------------

## Named Entity Recognition (NER)

NER identifies real‑world entities such as:

-   PERSON
-   ORGANIZATION
-   LOCATION
-   DATE

Example:

Input: John Smith works at Google

Output:

John Smith → PERSON\
Google → ORG

Used to extract names from resumes.

------------------------------------------------------------------------

# 5. Tokenization

Tokenization splits text into smaller units called tokens.

Example:

Input:

Machine learning engineer

Tokens:

Machine\
learning\
engineer

spaCy performs tokenization automatically.

------------------------------------------------------------------------

# 6. Keyword Extraction

Simple method:

Check if predefined keywords exist.

Example:

skills list:

python\
sql\
excel

If found → add to output.

Concept:

Rule‑based information extraction

------------------------------------------------------------------------

# 7. String Processing

Python allows:

Split text:

``` python
text.split('\n')
```

Convert case:

``` python
text.lower()
```

Remove spaces:

``` python
text.strip()
```

Concept:

Text normalization

------------------------------------------------------------------------

# 8. Data Structures

## Lists

Store multiple values

Example:

``` python
skills = ['python','sql']
```

------------------------------------------------------------------------

## Dictionaries

Store structured data

Example:

``` python
resume = {
 "name":"John",
 "skills":["python"]
}
```

Used in APIs and databases.

------------------------------------------------------------------------

# 9. Information Extraction Pipeline

This project follows a pipeline:

Document\
↓\
Text extraction\
↓\
Cleaning\
↓\
Pattern matching (regex)\
↓\
NLP extraction\
↓\
Structured output

This is called:

Information Extraction System

------------------------------------------------------------------------

# 10. Why NLP is needed

Regex works only for fixed patterns.

Names vary a lot.

Example:

Dr. John A. Smith\
John Smith

Regex fails.

NLP understands context.

------------------------------------------------------------------------
