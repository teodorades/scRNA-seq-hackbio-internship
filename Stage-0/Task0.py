"""
Task:
Write a simple Python script to print the
names, Slack usernames, countries, hobbies,
affiliations of people on your team, and the
DNA sequence of the genes they love most.

"""

import pandas as pd
# Fetch the sequence region from NCBI
from Bio import Entrez
import time

# Read the CSV file as a DataFrame (semicolon-separated)
df = pd.read_csv("team.csv", sep=';')

# Print the first few rows of the DataFrame
print("Full team data preview:")
print(df.head(), "\n")

# Print all names
print(f"Names: \n{df['name']}\n")

# Print all Slack usernames
print(f"Slack usernames: \n{df['username']}\n")

# Print countries
print(f"Countries: \n{df['country']}\n")

# Print hobbies
print(f"Hobbies: \n{df['hobby']}\n")

# Print affiliations
print(f"Affiliations: \n{df['affiliations']}\n")

# Print linkedin, github 
print(f"Linkedin: \n{df['linkedin_url']}\n \nGithub: \n{df['github_url']}\n")

# Print the data of one specific person:
print(f"Information for the first person: \n{df.iloc[0]}\n")


# Identification for NCBI access
Entrez.email = "teodoradespotovski@gmail.com"  

# Dictionary mapping team member - favorite gene
favorite_genes = {
    "Teodora": "NC_000010.11",      
    "Augusta": "NM_000546.6",      
    "Sultan": "RRCD01000101.1",       
    "Jovana": "NC_000913.3",    
    "Auwal": "NG_042857.2"         
}

# Loop through each team member and fetch their favorite gene
for name, acc in favorite_genes.items():
    print(f"Fetching {acc} for {name} ...")

    with Entrez.efetch(
        db="nuccore",
        id=acc,
        rettype="fasta",
        retmode="text"
    ) as handle:
        fasta_data = handle.read()

    # Create a filename like "Teodora_id.fasta"
    filename = f"{name}_{acc}.fasta"

    with open(filename, "w") as f:
        f.write(fasta_data)

    print(f"Saved {filename}\n")

    # Optional delay to respect NCBI rate limits
    time.sleep(1)

# Printing favorite genes, example:
file = "Teodora_NC_000010.11.fasta"

with open(file, "r") as f:
    content = f.read()

print(content)
