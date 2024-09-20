import openai
import sys

# Set your OpenAI API key here
openai.api_key = 'OPENAI_API_KEY'

def read_file_lines(filename):
    """Read and return the lines of a file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_file_lines(filename, lines):
    """Write lines to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def translate_chunk(chunk, sentence, model_version):
    # Handling the API call to OpenAI
    response = openai.chat.completions.create(
            model=model_version,
            messages=[
                {"role": "system", "content": "You are an experienced language tutor from Manila, well-versed in the Talalog language."},
                {"role": "user", "content": f"Explain the grammar of the given Tagalog text (labelled text1) to a Tagalog learner in English. Please keep the explanation short and crisp. Please give the explanation in one sentence only. Please omit connecting phrases such as (in the phrase). Please skip the conclusion. Just write as you are writing a footnote with limited space. Please add asterick in front and after each Tagalog word/phrase/wordchunk. For reference, I have also provided the sentence (labelled sentence1) from which text1 is derived. \n\nExample:\nExample Text1: Napakasamang lagay ng panahon\nExample Sentence1: Napakasamang Lagay ng Panahon—Paano Makakatulong ang Bibliya?\nExpected output: *Napakasamang lagay ng panahon* translates to Very bad weather, where *napakasama* is an intensifier meaning very bad, *lagay* means state or condition, and *ng panahon* indicates of the weather, showing possession. Conditions\n\nText1:{chunk}\nSentence1:{sentence}"}
            ],
            temperature=0
    )

    # Extracting the API response
    translation = response.choices[0].message.content.strip()

    if '\n' in translation:
        print(f"Multiple lines detected in ChatGPT response: {translation}. Retrying.")
        return translate_chunk(chunk, sentence, model_version)
    return translation

def process_file_pairs(original_filename, token_filename, model, output_suffix):
    """Process each line pair from given files, translate chunks, and write results to the output file."""
    original_lines = read_file_lines(original_filename)
    token_lines = read_file_lines(token_filename)

    if len(original_lines) != len(token_lines):
        print(f"Error: The files {original_filename} (lines: {len(original_lines)}) and {token_filename} (lines: {len(token_lines)}) don't have the same number of lines.")
        sys.exit(1)

    translated_lines = []

    for i in range(len(original_lines)):
        original_sentence = original_lines[i].strip()
        chunks = token_lines[i].strip().split(';')

        translated_chunks = []
        for j, chunk in enumerate(chunks):
            print(f"{i+1}: Passing {chunk} to ChatGPT model {model}")
            translated_chunk = translate_chunk(chunk, original_sentence, model)
            print(f"{i+1}: Receiving explanation from ChatGPT model {model}")
            translated_chunks.append(translated_chunk)

        translated_line = ';'.join(translated_chunks)
        translated_lines.append(translated_line + '\n')

    output_filename = f"{original_filename.split('.')[0]}{output_suffix}.txt"
    write_file_lines(output_filename, translated_lines)
    print(f"Written explanation to {output_filename}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <original_filename>")
        sys.exit(1)

    original_filename = sys.argv[1]
    token1_filename = f"{original_filename.split('.')[0]}-token1.txt"
    token2_filename = f"{original_filename.split('.')[0]}-token2.txt"

    process_file_pairs(original_filename, token1_filename, "gpt-4o-2024-08-06", "-token1-explained")
    process_file_pairs(original_filename, token2_filename, "gpt-4o-2024-05-13", "-token2-explained")

if __name__ == "__main__":
    main()