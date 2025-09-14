import re

phrase1 = "Je discute avec [<des personnes intéressantes>] comme toi."
phrase2 = "Je parle avec [<d’autres de mes utilisateur>] !"

# Récupérer les éléments interchangeables
elem1 = re.search(r"\[<(.*?)>\]", phrase1).group(1)
elem2 = re.search(r"\[<(.*?)>\]", phrase2).group(1)

# Générer les phrases mélangées
new_phrase1 = re.sub(r"\[<.*?>\]", elem2, phrase1)
new_phrase2 = re.sub(r"\[<.*?>\]", elem1, phrase2)

print(new_phrase1)
print(new_phrase2)
