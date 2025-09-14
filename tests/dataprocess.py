from sentence_transformers import SentenceTransformer
import json

# Charger le modèle
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def add_embeddings(json_path, output_path):
    # 1. Lire le JSON
    with open(json_path, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    # 2. Ajouter l'embedding à chaque question
    for item in dataset:
        question = item["Q"]
        embedding = model.encode(question, convert_to_tensor=False)  # tensor=False pour JSON
        item["embedding"] = embedding.tolist()  # On convertit en liste pour pouvoir sauvegarder en JSON

    # 3. Réécrire le JSON avec les embeddings
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=4)

    print(f"Embeddings ajoutés et sauvegardés dans {output_path}")

# Exemple d'utilisation
add_embeddings("0.5/dataset/qa.json", "0.5/dataset/qa_with_embeddings.json")
