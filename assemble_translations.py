import os
import sys

def check_files(base_filename):
    suffixes = [
        "", "_translated_full_sentences", "-token1", "-token1-explained", "-token1-translated",
        "-token2", "-token2-explained", "-token2-translated"
    ]
    for suffix in suffixes:
        filename = f"{base_filename}{suffix}.txt"
        if not os.path.isfile(filename):
            print(f"Error: {filename} not found.")
            return False
    return True

def read_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

def create_markdown(base_filename):
    # Read all files
    original_lines = read_lines(f"{base_filename}.txt")
    translated_full_sentences_lines = read_lines(f"{base_filename}_translated_full_sentences.txt")
    token1_lines = read_lines(f"{base_filename}-token1.txt")
    token1_explained_lines = read_lines(f"{base_filename}-token1-explained.txt")
    token1_translated_lines = read_lines(f"{base_filename}-token1-translated.txt")
    token2_lines = read_lines(f"{base_filename}-token2.txt")
    token2_explained_lines = read_lines(f"{base_filename}-token2-explained.txt")
    token2_translated_lines = read_lines(f"{base_filename}-token2-translated.txt")

    # Check if all files have the same number of lines
    num_lines = len(original_lines)
    if not all(len(lines) == num_lines for lines in [
        translated_full_sentences_lines, token1_lines, token1_explained_lines, token1_translated_lines,
        token2_lines, token2_explained_lines, token2_translated_lines
    ]):
        print("Error: Not all files have the same number of lines.")
        return

    # Create markdown file
    with open(f"{base_filename}.md", 'w', encoding='utf-8') as md_file:
        for i in range(num_lines):
            print(f"Processing line {i + 1}/{num_lines}...")

            # Original line
            original_line = original_lines[i].strip()
            md_file.write(f"#{i + 1}\n")
            md_file.write(f"**{original_line}**\n")

            # Translated full sentences
            translated_full_sentences = translated_full_sentences_lines[i].strip().split(';')
            md_file.write(f"{translated_full_sentences[0]}\n")
            md_file.write(f"{translated_full_sentences[1]}\n\n")

            # Token1 table
            token1_tokens = token1_lines[i].strip().split(';')
            token1_translations = token1_translated_lines[i].strip().split(';')
            token1_explanations = token1_explained_lines[i].strip().split(';')
            md_file.write("| Token | Translation | Explanation |\n")
            md_file.write("|-------|-------------|-------------|\n")
            for token, translation, explanation in zip(token1_tokens, token1_translations, token1_explanations):
                md_file.write(f"| {token} | {translation} | {explanation} |\n")
            md_file.write("\n")

            # Token2 table
            token2_tokens = token2_lines[i].strip().split(';')
            token2_translations = token2_translated_lines[i].strip().split(';')
            token2_explanations = token2_explained_lines[i].strip().split(';')
            md_file.write("| Token | Translation | Explanation |\n")
            md_file.write("|-------|-------------|-------------|\n")
            for token, translation, explanation in zip(token2_tokens, token2_translations, token2_explanations):
                md_file.write(f"| {token} | {translation} | {explanation} |\n")
            md_file.write("\n")
            md_file.write("---\n\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <base_filename>")
        sys.exit(1)

    base_filename = sys.argv[1].replace('.txt', '')

    if not check_files(base_filename):
        sys.exit(1)

    create_markdown(base_filename)
    print(f"Markdown file {base_filename}.md created successfully.")