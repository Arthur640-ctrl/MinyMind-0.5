# -*- coding: utf-8 -*-
import re

# Liste simplifiée de mots-clés qui signalent un calcul
keywords = [
    "calculer", "combien", "résoudre", "évaluer", "additionner", 
    "soustraire", "multiplier", "diviser", "somme", "différence", 
    "produit", "quotient", "total", "moyenne", "racine", "puissance"
]

def is_calculation_request(user_input):
    user_input_lower = user_input.lower()
    for word in keywords:
        if word in user_input_lower:
            return True
    # On peut aussi détecter des expressions purement numériques
    if re.search(r"\d+[\+\-\*\/\^]", user_input):  # ex: 3+5, 2*7, 4^2
        return True
    return False

def extract_expression(user_input):
    # On ne garde que les chiffres et opérateurs classiques
    expression = re.sub(r"[^0-9\+\-\*\/\.\(\)\^]", "", user_input)
    # Remplacer ^ par ** pour Python
    expression = expression.replace("^", "**")
    return expression

while True:
    user_input = input("💬 Tape quelque chose (ou 'exit' pour quitter) : ")
    if user_input.lower() == "exit":
        print("Au revoir ! 👋")
        break
    
    if is_calculation_request(user_input):
        try:
            expr = extract_expression(user_input)
            if expr == "":
                print("❌ Je n'ai pas trouvé d'expression à calculer.")
            else:
                result = eval(expr)
                print(f"✅ Résultat : {result}")
        except Exception as e:
            print(f"❌ Impossible de calculer : {e}")
    else:
        print("ℹ️ Pas un calcul détecté.")
