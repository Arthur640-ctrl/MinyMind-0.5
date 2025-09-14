import json

# Chemin vers ton fichier JSON
file_path = "data/qa.json"

# Ouvrir et lire le fichier JSON
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Nombre de questions
num_questions = len(data)

# Nombre total de réponses
num_answers = sum(len(entry.get("A", [])) for entry in data)

print(f"Nombre de questions (Q) : {num_questions}")
print(f"Nombre total de réponses (A) : {num_answers}")
