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

def calculate_cost(tokens, rate_per_1k_tokens):
    return (tokens / 1000) * rate_per_1k_tokens

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

    total_token_count = prompt_input_token_count + prompt_output_token_count

    # Rates and conversion
    input_rate_per_1k_tokens = 0.005
    output_rate_per_1k_tokens = 0.015
    api_call_cost = 0.0080
    usd_to_idr = 16500

    input_cost_usd = calculate_cost(prompt_input_token_count, input_rate_per_1k_tokens)
    output_cost_usd = calculate_cost(prompt_output_token_count, output_rate_per_1k_tokens)
    total_cost_usd = input_cost_usd + output_cost_usd + api_call_cost

    input_cost_idr = input_cost_usd * usd_to_idr
    output_cost_idr = output_cost_usd * usd_to_idr
    total_cost_idr = total_cost_usd * usd_to_idr

    print(f"Input Token Count: {prompt_input_token_count}")
    print(f"Output Token Count: {prompt_output_token_count}")
    print(f"Total Token Count: {total_token_count}")
    print(f"Rp for Input: Rp {input_cost_idr:.2f}")
    print(f"Rp for Output: Rp {output_cost_idr:.2f}")
    print(f"Rp for Total (including API Call): Rp {total_cost_idr:.2f}")
