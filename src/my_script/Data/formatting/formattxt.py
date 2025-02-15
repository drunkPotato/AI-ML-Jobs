import re

#Program Description:

#Seperate the individual listings from each other (depending on the website this differs)
#Remove the newlines & other trailing whitespaces in each listing (formatting)
#Check for Relevance (relevance)
#Check for Duplicates (duplicate)
#Add an ID in front of the individual joblistings

def write_to_file(input_file, output_file):


    # Read the content of the input file
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile:
        text = infile.read()


    # Remove all newlines and extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Add two newlines before "Job overview"
    text = re.sub(r'(Find out how your skills align with the job description)', r'\n\n\1', text)

    # Define the pattern to identify the start of each job description
    pattern = re.compile(r'(?=\n\n)')

    parts = pattern.split(text)
    for i in range(1, len(parts)):
        parts[i] = f'\n\n\nMy ID: 08084{i} ' + parts[i].strip()

    # Join the parts back together
    text = ''.join(parts)

    # Format the text to have a newline every 150 characters
    text = '\n'.join(text[i:i+150] for i in range(0, len(text), 150))

    # Write the processed text to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(text)

input_file = 'src/my_script/Data/txtfiles/raw/Indeed_US.txt'
output_file = 'src/my_script/Data/txtfiles/formatted/fIndeed_US.txt'

write_to_file(input_file, output_file)
