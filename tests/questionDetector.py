import spacy

# Charger le modèle français
nlp = spacy.load("fr_core_news_sm")

# Exemple
phrase = "Le chat mange la souris."
doc = nlp(phrase)

for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
