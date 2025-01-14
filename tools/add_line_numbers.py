import sys

def add_line_numbers(input_file, output_file):
    """
    Adds line numbers to each line in the input file and writes to the output file.
    
    :param input_file: Path to the input file
    :param output_file: Path to the output file
    """
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for i, line in enumerate(infile, start=1):
                outfile.write(f"{i}. {line}")
        print(f"Numbered lines have been written to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Command-line arguments
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python add_line_numbers.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        add_line_numbers(input_file, output_file)

