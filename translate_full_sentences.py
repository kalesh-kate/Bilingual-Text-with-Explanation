import sys
import openai

# Set your OpenAI API key here
openai.api_key = 'OPENAI_API_KEY'

def translate_sentence(sentence, system_prompt, user_prompt, model_prompt):
    try:
        response = openai.chat.completions.create(
            model=model_prompt,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt.format(sentence=sentence)}
            ],
            temperature=0
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error translating sentence: {e}")
        return ""

def main(input_file):
    output_file = input_file.replace('.txt', '_translated_full_sentences.txt')
    
    # System prompts for the two translations
    system_prompt_1 = "You are a native speaker of Tagalog from Manila and you are skilled in translating Tagalog into grammatically correct English. You are always good at finding the most precise but natural sounding English translation for each Tagalog word."
    user_prompt_1 = "Please translate the given sentence in natural sounding English, but as faithful to the original sentence as possible. \n\n Given sentence: {sentence}\n\nPlease provide the output in one line only."
    model_prompt_1 = "gpt-4o-2024-08-06"

    system_prompt_2 = "You are a native speaker of Tagalog from Manila and you are skilled in translating Tagalog into grammatically correct English. You are always good at finding the most precise but natural sounding English translation for each Tagalog word."
    user_prompt_2 = "Please translate the given sentence in natural sounding English, but as faithful to the original sentence as possible. \n\n Given sentence: {sentence}\n\nPlease provide the output in one line only."
    model_prompt_2 = "gpt-4o-2024-05-13"

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            sentence = line.strip()
            if sentence:
                print(f"Translating: {sentence}")
                
                # First translation
                translation_1 = translate_sentence(sentence, system_prompt_1, user_prompt_1, model_prompt_1)
                print(f"Translation 1: {translation_1}")
                
                # Second translation
                translation_2 = translate_sentence(sentence, system_prompt_2, user_prompt_2, model_prompt_2)
                print(f"Translation 2: {translation_2}\n")
                
                # Write to output file
                outfile.write(f'"{translation_1}";"{translation_2}"\n')

    print(f"Translations completed. Output written to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python translate_full_sentences.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)