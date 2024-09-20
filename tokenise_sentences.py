import os
import sys
import openai

# Set up your OpenAI API key here
openai.api_key = 'OPENAI_API_KEY'

def process_sentence(sentence, model_version):
    """Function to process a single sentence with the specified ChatGPT model."""
    try:
        response = openai.chat.completions.create(
            model=model_version,
            messages=[
                {"role": "system", "content": "You are a NLP researcher from Metro Manila, well-versed in the Tagalog language and its slang."},
                {"role": "user", "content": f"Please break this Tagalog sentence into meaningful chunks, separating them with semicolons.\n\nFor example: 'Isa ka ba sa milyon-milyong tao na apektado ng napakasamang lagay ng panahon?' \n\nI expect the output to look like: 'Isa ka ba; sa milyon-milyong tao; na apektado; ng napakasamang lagay ng panahon?' \n\nPlease provide the output in one line.\n\nSentence: {sentence}"}
            ],
            temperature=0
        )
        output = response.choices[0].message.content.strip()
        return output
    except Exception as e:
        print(f"Error processing the sentence: {e}")
        return None

def write_to_file(line_num, output, filepath):
    """Function to write the output to a specified file."""
    try:
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(output + '\n')
        print(f"{line_num}: Writing the output to text file {filepath}.")
    except Exception as e:
        print(f"Error writing to file {filepath}: {e}")

def main(file_path):
    # Open the input file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            sentences = file.readlines()
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return

    # Output file names based on input file path
    base_name = os.path.splitext(file_path)[0]
    output_file1 = f"{base_name}-token1.txt"
    output_file2 = f"{base_name}-token2.txt"

    for line_num, sentence in enumerate(sentences, start=1):
        # Strip newline characters and extra spaces
        sentence = sentence.strip()

        # Process with the first model
        print(f"{line_num}: Passing {sentence} to ChatGPT model gpt-4o-2024-08-06.")
        output1 = process_sentence(sentence, "gpt-4o-2024-08-06")

        if output1 and '\n' not in output1:  # Ensure it is single line
            print(f"{line_num}: Receiving {output1} from ChatGPT model gpt-4o-2024-08-06.")
            write_to_file(line_num, output1, output_file1)
        else:
            print(f"Error: Output from model gpt-4o-2024-08-06 is not a single line for sentence: {sentence}. Retrying...")
            continue

        # Process with the second model
        print(f"{line_num}: Passing {sentence} to ChatGPT model gpt-4o-2024-05-13.")
        output2 = process_sentence(sentence, "gpt-4o-2024-05-13")

        if output2 and '\n' not in output2:  # Ensure it is single line
            print(f"{line_num}: Receiving {output2} from ChatGPT model gpt-4o-2024-05-13.")
            write_to_file(line_num, output2, output_file2)
        else:
            print(f"Error: Output from model gpt-4o-2024-05-13 is not a single line for sentence: {sentence}. Retrying...")
            continue

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    main(file_path)