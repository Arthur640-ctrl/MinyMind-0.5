from sentence_transformers import SentenceTransformer, util

# 1. Charger un modèle multilingue (prend en charge le français)
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# 2. Les phrases à comparer
phrase1 = "sciences"
phrase2 = "C'est quoi la physique quantique ?"

# 3. Générer les embeddings
embedding1 = model.encode(phrase1, convert_to_tensor=True)
embedding2 = model.encode(phrase2, convert_to_tensor=True)


# 4. Calculer la similarité cosinus
similarity = util.cos_sim(embedding1, embedding2).item()

print(f"Similarité : {similarity:.4f}")
print(f"Embeding {phrase1} : {embedding1}")
print(f"Embeding {phrase2} : {embedding2}")


# Interprétation simple
# if similarity > 0.8:
#     print("Les phrases veulent dire la même chose :white_check_mark:")
# elif similarity > 0.5:
#     print("Les phrases sont liées, mais pas identiques :thinking:")
# else:
#     print("Les phrases sont différentes :x:")