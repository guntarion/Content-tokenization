import sys
import os
import tiktoken

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def count_tokens(text):
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
    return len(tokens)

if __name__ == "__main__":
    folder_path = './documents'
    
    prompt_input_file = 'prompt_input.txt'
    prompt_output_file = 'prompt_output.txt'
    
    prompt_input_path = os.path.join(folder_path, prompt_input_file)
    prompt_output_path = os.path.join(folder_path, prompt_output_file)

    if not os.path.isfile(prompt_input_path):
        print(f"File not found: {prompt_input_path}")
        sys.exit(1)
    
    if not os.path.isfile(prompt_output_path):
        print(f"File not found: {prompt_output_path}")
        sys.exit(1)
    
    prompt_input_text = read_file(prompt_input_path)
    prompt_output_text = read_file(prompt_output_path)

    prompt_input_token_count = count_tokens(prompt_input_text)
    prompt_output_token_count = count_tokens(prompt_output_text)

    print(f"Prompt Input Token count: {prompt_input_token_count}")
    print(f"Prompt Output Token count: {prompt_output_token_count}")
