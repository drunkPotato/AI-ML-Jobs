import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Read the file containing job listings
with open('src/my_script/Data/txtfiles/formatted/jobs_ch.txt', 'r', encoding='utf-8') as file:
    content = file.read()

listings = re.split(r'\n\n', content.lower())

for listing in listings:
    listing = listing.replace('\n', ' ')

df = pd.DataFrame(listings, columns=['job_description'])

print(df.shape[0])

# Step 4: Tokenization and Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['job_description'])

# Step 5: Calculate similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Step 6: Identify duplicates
threshold = 0.9 # Similarity threshold
unique_indices = []
for i in range(cosine_sim.shape[0]):
    is_unique = True
    for j in range(i):
        if cosine_sim[i, j] > threshold:
            is_unique = False
            break
    if is_unique:
        unique_indices.append(i)

# Extract unique job listings
unique_listings = df.iloc[unique_indices]['job_description']

print(len(unique_listings))

# Step 7: Save unique listings to a new file
with open('src/my_script/Data/txtfiles/final/sjobs_ch.txt', 'w', encoding='utf-8') as file:
    for listing in unique_listings:
        file.write(listing + '\n\n')  # Ensure each listing is separated by two newlines

print("Unique job listings have been saved to 'unique_job_listings.txt'.")