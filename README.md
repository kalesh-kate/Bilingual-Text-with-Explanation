# Bilingual-Text-with-Explanation
A series of Python scripts that take a list of sentences, translate them fully and in chunks using ChatGPT api, and output them to a markdown file that displays nicely in Obsidian.

![Example 1](https://github.com/kalesh-kate/Bilingual-Text-with-Explanation/blob/main/example_1.jpg?raw=true)

![Example 2](https://github.com/kalesh-kate/Bilingual-Text-with-Explanation/blob/main/example_2.jpg?raw=true)

# Introduction

This manual provides a step-by-step guide on how to use the Bilingual Text with Explanation pipeline implemented in Python scripts for language learning. The main program, `main.py`, orchestrates the execution of several scripts that handle translation, tokenization, explanation, and assembly of translations.

**Please note that the prompts from the scripts are designed for compiling Tagalog text. For translating other languages, please adjust the prompts by following the instructions in the 'Steps to Change the Language' section**

## Overview of the Pipeline

The pipeline consists of the following scripts:

1. **`translate_full_sentences.py`**: Translates full sentences.

2. **`tokenise_sentences.py`**: Breaks down sentences into meaningful chunks (tokens).

3. **`translate_tokens.py`**: Translates the tokens into English.

4. **`explain_tokens.py`**: Provides explanations for the tokens in English.

5. **`assemble_translations.py`**: Assembles all the translations and explanations into a markdown file.

## Getting Started

### Prerequisites

1. **Python**: Ensure you have Python installed on your machine.

2. **OpenAI API Key**: You need an OpenAI API key to use the translation services. Replace the placeholder in each script with your actual API key.

3. **OpenAI package**: The OpenAI Python package must be installed. You can install it using the following command:`pip install openai`

### Directory Structure

Make sure your directory contains the following files:

- `main.py`

- `translate_full_sentences.py`

- `tokenise_sentences.py`

- `translate_tokens.py`

- `explain_tokens.py`

- `assemble_translations.py`

- An input text file (e.g., `input.txt`) containing Tagalog sentences to be translated.

### Running the Pipeline

1. **Open a terminal**.

2. **Navigate to the directory** where your scripts are located.

3. **Run the main script** with the input filename as an argument:

```bash

python main.py input.txt

```

Replace `input.txt` with the name of your input file.

### What Happens Next

The `main.py` script will execute the following steps in order:

1. **Translate Full Sentences**: Calls `translate_full_sentences.py` to translate each sentence in the input file.

2. **Tokenize Sentences**: Calls `tokenise_sentences.py` to break down the translated sentences into tokens.

3. **Translate Tokens**: Calls `translate_tokens.py` to translate each token into English.

4. **Explain Tokens**: Calls `explain_tokens.py` to provide explanations for each token.

5. **Assemble Translations**: Calls `assemble_translations.py` to compile all translations and explanations into a markdown file.

### Output Files

After running the pipeline, you will find the following output files in the same directory:

- `input_translated_full_sentences.txt`: Contains the translations of the full sentences.

- `input-token1.txt`: Contains the first set of tokenized sentences.

- `input-token1-explained.txt`: Contains explanations for the first set of tokens.

- `input-token1-translated.txt`: Contains translations for the first set of tokens.

- `input-token2.txt`: Contains the second set of tokenized sentences.

- `input-token2-explained.txt`: Contains explanations for the second set of tokens.

- `input-token2-translated.txt`: Contains translations for the second set of tokens.

- `input.md`: A markdown file that assembles all the translations and explanations.

### Cleaning Up Temporary Files

The `main.py` script automatically deletes temporary files after processing. If you want to keep any of the intermediate files, you can comment out the deletion section in `main.py`.

## Troubleshooting

- **File Not Found**: Ensure that the input file exists in the same directory as the scripts.

- **API Errors**: If you encounter errors related to the OpenAI API, check your API key and ensure you have access to the required models.

- **Line Count Mismatch**: If the number of lines in the output files does not match, check the input file for empty lines or formatting issues.

### Steps to Change the Language

1. **Update Prompts in `translate_full_sentences.py`**:

- Modify the system and user prompts to reflect the new target language. For example, if you want to translate from Tagalog to German, you would change the prompts accordingly.

**Example for German**:

```python

system_prompt_1 = "You are a native speaker of German and you are skilled in translating German into grammatically correct English."

user_prompt_1 = "Please translate the given sentence into natural-sounding English, but as faithful to the original sentence as possible. \n\n Given sentence: {sentence}\n\nPlease provide the output in one line only."

```

**Example for Hindi**:

```python

system_prompt_1 = "You are a native speaker of Hindi and you are skilled in translating Hindi into grammatically correct English."

user_prompt_1 = "Please translate the given sentence into natural-sounding English, but as faithful to the original sentence as possible. \n\n Given sentence: {sentence}\n\nPlease provide the output in one line only."

```

2. **Update Prompts in `tokenise_sentences.py`**:

- Similar to the previous step, update the prompts to reflect the new language for tokenization.

**Example for German**:

```python

response = openai.chat.completions.create(

model=model_version,

messages=[

{"role": "system", "content": "You are an NLP researcher from Germany, well-versed in the German language."},

{"role": "user", content: f"Please break this German sentence into meaningful chunks, separating them with semicolons.\n\nSentence: {sentence}"}

],

temperature=0

)

```

**Example for Hindi**:

```python

response = openai.chat.completions.create(

model=model_version,

messages=[

{"role": "system", "content": "You are an NLP researcher from India, well-versed in the Hindi language."},

{"role": "user", content: f"Please break this Hindi sentence into meaningful chunks, separating them with semicolons.\n\nSentence: {sentence}"}

],

temperature=0

)

```

3. **Update Prompts in `translate_tokens.py` and `explain_tokens.py`**:

- Update the prompts in these scripts to ensure that the translations and explanations are tailored to the new language.

**Example for German**:

```python

response = openai.chat.completions.create(

model=model_version,

messages=[

{"role": "system", "content": "You are a native speaker of German."},

{"role": "user", content: f"Translate the text into English. Text: {chunk}."}

],

temperature=0

)

```

**Example for Hindi**:

```python

response = openai.chat.completions.create(

model=model_version,

messages=[

{"role": "system", "content": "You are a native speaker of Hindi."},

{"role": "user", content: f"Translate the text into English. Text: {chunk}."}

],

temperature=0

)

```

4. **Update the Input File**:

- Ensure that the input text file contains sentences in the new source language (e.g., German or Hindi) that you want to translate.

5. **Run the Pipeline**:

- After making the necessary changes, run the `main.py` script as before, using the input file with the new language sentences.

```bash

python main.py input_german.txt

```

or

```bash

python main.py input_hindi.txt

```
