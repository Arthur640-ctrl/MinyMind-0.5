import json

# Chemin vers ton fichier JSON
file_path = "data/qa.json"

# Lire le fichier JSON
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Supprimer les doublons
seen_questions = set()
unique_data = []

for entry in data:
    question = entry["Q"]
    if question not in seen_questions:
        unique_data.append(entry)
        seen_questions.add(question)

# Écrire le fichier JSON sans doublons
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(unique_data, f, ensure_ascii=False, indent=4)

print(f"Avant : {len(data)} questions")
print(f"Après suppression des doublons : {len(unique_data)} questions")
