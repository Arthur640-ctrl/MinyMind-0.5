from transformers import pipeline

# Modèle public, gratuit et accessible sans login
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"

# Création du pipeline
classifier = pipeline("text-classification", model=model_name, tokenizer=model_name)

print("=== Détecteur de style/humeur ===")
print("Tape 'quit' pour quitter.\n")

def star_to_humeur(label):
    mapping = {
        "1 star": "triste / négatif",
        "2 stars": "un peu négatif",
        "3 stars": "neutre",
        "4 stars": "positif",
        "5 stars": "très positif"
    }
    return mapping.get(label, "inconnu")


while True:
    phrase = input("Entrez une phrase : ")
    if phrase.lower() == "quit":
        break

    result = classifier(phrase)[0]

    humeur = star_to_humeur(result['label'])
    print(f"Humeur détectée → {humeur} ({result['score']:.2f})\n")

