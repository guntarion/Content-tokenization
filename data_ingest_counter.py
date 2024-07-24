import sys
import fitz  # PyMuPDF
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

def split_text_into_chunks(text, max_tokens_per_chunk=1000):
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
    chunks = []
    for i in range(0, len(tokens), max_tokens_per_chunk):
        chunk = tokens[i:i + max_tokens_per_chunk]
        chunks.append(enc.decode(chunk))
    return chunks

def calculate_cost(tokens, rate_per_1k_tokens):
    return (tokens / 1000) * rate_per_1k_tokens

if __name__ == "__main__":
    folder_path = './documents'
    filename = 'Contoh_Dokumen_A4_100_halaman.pdf'  # Change this to your PDF file name
    pdf_path = os.path.join(folder_path, filename)

    if not os.path.isfile(pdf_path):
        print(f"File not found: {pdf_path}")
        sys.exit(1)

    text = extract_text_from_pdf(pdf_path)
    chunks = split_text_into_chunks(text)
    
    total_token_count = sum(count_tokens(chunk) for chunk in chunks)
    
    # Rates and conversion
    embedding_rate_per_1k_tokens = 0.00013
    usd_to_idr = 16500

    total_cost_usd = calculate_cost(total_token_count, embedding_rate_per_1k_tokens)
    total_cost_idr = total_cost_usd * usd_to_idr

    print(f"Total Token Count: {total_token_count}")
    print(f"Total Cost in USD: ${total_cost_usd:.6f}")
    print(f"Total Cost in IDR: Rp {total_cost_idr:.2f}")
