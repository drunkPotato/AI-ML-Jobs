import re
def write_to_file(input_file, output_file):
    # Read the content of the input file
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile:
        text = infile.read()


    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
    #text = ' '.join(text.split())

    # Define the pattern to identify the start of each job description
    pattern = re.compile(r'(?=\n\n\n)')

    parts = pattern.split(text)
    for i in range(1, len(parts)):
        parts[i] = f'\n\n\nMy ID: 28073{i} \n' + parts[i].strip()


    # Join the parts back together
    text = ''.join(parts)

    # Add two new lines before the pattern
    #text = pattern.sub('\n\n\n', text)
    
    text = '\n'.join(text[i:i+150] for i in range(0, len(text), 150))

    # Write the processed text to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(text)


input_file = 'src/my_script/Data/txtfiles/formatted/formatedjobs_ch.txt'
output_file = 'src/my_script/Data/txtfiles/formatted/formattedjobs_ch.txt'

write_to_file(input_file, output_file)
