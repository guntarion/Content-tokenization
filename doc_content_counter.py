import sys
import fitz  # PyMuPDF
import re
import os
import tiktoken

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def count_tokens(text):
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
    return len(tokens)

def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def count_characters(text):
    return len(text)

if __name__ == "__main__":
    folder_path = './documents'
    filename = 'Contoh_Dokumen_A4_100_halaman.pdf'  # Change this to your PDF file name
    pdf_path = os.path.join(folder_path, filename)

    if not os.path.isfile(pdf_path):
        print(f"File not found: {pdf_path}")
        sys.exit(1)

    text = extract_text_from_pdf(pdf_path)

    token_count = count_tokens(text)
    word_count = count_words(text)
    character_count = count_characters(text)

    print(f"Token count: {token_count}")
    print(f"Word count: {word_count}")
    print(f"Character count: {character_count}")
