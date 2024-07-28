from langdetect import detect
import re
from collections import Counter
import time

# Function to extract text following "Job description"
def extract_job_description(text):
    # Search for the exact phrase "Job description"
    match = re.search(r'Job description', text, re.DOTALL)
    if match:
        # Find the position immediately after "Job description"
        start_index = match.end()
        # Extract the first 150 characters after the phrase
        description_text = text[start_index:start_index + 150].strip()
        return description_text
    return ""

# Read the job listings from the file
with open("src/my_script/Data/txtfiles/formated2307eures.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Split the content into individual job listings
job_listings = content.split("\n\n")

# Function to detect the language of the extracted job description text
def detect_language(text):
    try:
        return detect(text)
    except Exception as e:
        print(f"Detection error: {e}")
        return "unknown"

# Measure the time taken for language detection
start_time = time.time()

# Detect languages for the text following "Job description"
languages = [detect_language(extract_job_description(listing)) for listing in job_listings]

end_time = time.time()

# Count the occurrences of each language
language_counts = Counter(languages)

# Print the results
print("Language distribution based on job descriptions:")
for language, count in language_counts.items():
    print(f"{language}: {count}")

print(f"Time taken: {end_time - start_time} seconds")

# Optionally, print a few extracted texts for debugging
for i, listing in enumerate(job_listings[:10]):
    extracted_text = extract_job_description(listing)
    if extracted_text:
        print(f"Extracted text {i+1}: {extracted_text[:200]}")  # Print first 200 characters
