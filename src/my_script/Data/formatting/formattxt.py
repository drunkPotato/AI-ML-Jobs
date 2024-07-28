import re
def write_to_file(input_file, output_file):
    # Read the content of the input file
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile:
        text = infile.read()


    text = ' '.join(text.split())
    # Remove newlines and trailing whitespace
    #text = '\n'.join(line.strip() for line in text.strip().split('\n') if line.strip())
    # Split text into lines of 150 characters
#    lines = [text[i:i + 150] for i in range(0, len(text), 150)]
    #text = '\n'.join(text)

    # Define the pattern to identify the start of each job description
    pattern = re.compile(r'(?=Stellenbeschreibung Gleichen Sie hier die Stellenbeschreibung mit Ihrem Profil ab.)')

    # Add two new lines before the pattern
    text = pattern.sub('\n\n\n', text)
    text = '\n'.join(text[i:i+150] for i in range(0, len(text), 150))

    # Write the processed text to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(text)


# Example usage
input_file = 'src/my_script/Data/txtfiles/raw/Indeedartificialintelligence.txt'
output_file = 'src/my_script/Data/txtfiles/formatted/formattedIndeed_artificialIntelligence.txt'

write_to_file(input_file, output_file)
