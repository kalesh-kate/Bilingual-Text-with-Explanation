import os
import sys
import subprocess

def run_command(command):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Error: Command '{command}' failed with return code {result.returncode}")
        sys.exit(result.returncode)

def delete_file(filename):
    if os.path.exists(filename):
        print(f"Deleting: {filename}")
        os.remove(filename)
    else:
        print(f"File not found, skipping: {filename}")

def main(filename):
    commands = [
        f"python translate_full_sentences.py {filename}",
        f"python tokenise_sentences.py {filename}",
        f"python translate_tokens.py {filename}",
        f"python explain_tokens.py {filename}",
        f"python assemble_translations.py {filename}"
    ]

    for command in commands:
        run_command(command)

    base_filename = os.path.splitext(filename)[0]
    temp_files = [
        f"{base_filename}_translated_full_sentences.txt",
        f"{base_filename}-token1.txt",
        f"{base_filename}-token1-explained.txt",
        f"{base_filename}-token1-translated.txt",
        f"{base_filename}-token2.txt",
        f"{base_filename}-token2-explained.txt",
        f"{base_filename}-token2-translated.txt"
    ]

    for temp_file in temp_files:
        delete_file(temp_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    input_filename = sys.argv[1]
    main(input_filename) 