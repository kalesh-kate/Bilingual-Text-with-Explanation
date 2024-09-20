import sys
import os

def split_file(filename, lines_per_file):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        return

    total_lines = len(lines)
    num_files = (total_lines + lines_per_file - 1) // lines_per_file  # Calculate the number of files needed

    base_filename, file_extension = os.path.splitext(filename)
    bat_filename = f"{base_filename}.bat"

    with open(bat_filename, 'w') as bat_file:
        for i in range(num_files):
            start_line = i * lines_per_file
            end_line = start_line + lines_per_file
            chunk_lines = lines[start_line:end_line]

            output_filename = f"{base_filename}_{i+1:02d}.txt"
            with open(output_filename, 'w') as output_file:
                output_file.writelines(chunk_lines)

            print(f"Created {output_filename} with lines {start_line + 1} to {min(end_line, total_lines)}")
            bat_file.write(f"call python generate_markdown.py {output_filename}\n")

    print(f"Created {bat_filename} to run generate_markdown.py on each generated file.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python split_file.py <filename> <lines_per_file>")
        sys.exit(1)

    input_filename = sys.argv[1]
    try:
        lines_per_file = int(sys.argv[2])
    except ValueError:
        print("Error: The number of lines per file must be an integer.")
        sys.exit(1)

    split_file(input_filename, lines_per_file)