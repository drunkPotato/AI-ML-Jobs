# Define the keywords to search for
keywords = [
    #Deutsch
    "Künstliche Intelligenz", "Maschinelles Lernen", "Neuronale Netzwerke", "Datenwissenschaft", "Computer Vision",
    "Datenwissenschaftler", "KI-Ingenieur", "ML-Ingenieur",

    #French
    "Intelligence Artificielle", "Apprentissage Automatique", "Réseaux Neuronaux", "Science des Données", "Vision par Ordinateur",
    "Scientifique des Données", "Ingénieur en IA", "Ingénieur en Apprentissage Automatique",

    #English
    "Artificial Intelligence", "Machine Learning", "Neural Networks", "Data Science", "Computer Vision",
    "Data Scientist", "AI Engineer", "ML Engineer", 

    #Italian
    "Intelligenza Artificiale", "Apprendimento Automatico", "Reti Neurali", "Scienza dei Dati", "Visione Artificiale",
    "Scienziato dei Dati", "Ingegnere IA", "Ingegnere ML"
]

# Function to check if a job listing contains any of the keywords
def contains_keywords(job_listing, keywords):
    for keyword in keywords:
        if keyword.lower() in job_listing.lower():
            return True
    return False

# Read the job listings from the file
with open("src/my_script/Data/txtfiles/relevance/sjobs_ch.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Split the content into individual job listings
job_listings = content.split("\n\n")

# Filter the job listings based on the keywords
filtered_listings = [listing for listing in job_listings if contains_keywords(listing, keywords)]

# Write the filtered job listings to a new file
with open("src/my_script/Data/txtfiles/final/sjobs_ch.txt", "w", encoding="utf-8") as file:
    for listing in filtered_listings:
        file.write(listing + "\n\n")