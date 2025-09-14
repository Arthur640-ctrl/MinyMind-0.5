from sentence_transformers import SentenceTransformer, util
import re

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

calc_keywords = [
    # Mots liés aux calculs
    "calcule", "calcul", "additionne", "multiplie", "soustrait", "divise",
    "ajoute", "addition", "soustraction", "multiplication", "division",
    "somme", "résultat", "donne moi", "fait le calcul", "combien fait",

    # Symboles et opérateurs
    "+", "-", "*", "x", ":", "/", "=", "^",

    # Phrases courantes
    "combien font", "peux tu calculer", "quelle est la somme de",
    "fais la multiplication", "fais la division", "donne le résultat de",
    "résous", "résous ce calcul", "résous cette équation"
]

def dispatch(prompt, calcResultDebug = False, resultScore = False, finalChoice = False):
    
    promptEmbeding = model.encode(prompt, convert_to_tensor=True)

    if finalChoice and resultScore:
        print("========== Similarity Check ==========")

    calcScore = 0
    totalKeyword = len(calc_keywords)
    containsNumber = bool(re.search(r'\d+', prompt))

    
    for keyword in calc_keywords:
        keywordEmbeding = model.encode(keyword, convert_to_tensor=True)
        
        similarity = util.cos_sim(keywordEmbeding, promptEmbeding).item()
        
        calcScore += similarity

        if calcResultDebug:
            print(f"| Word : '{keyword}' : {similarity}")

    promptSlice = re.findall(r"\b\w+\b", prompt)
    promptLength = len(promptSlice)

    calcScore = calcScore / totalKeyword

    if containsNumber:
        calcScore *= 1.2

    if promptLength <= 2:         
        calcScore *= 0.5          
    elif promptLength >= 10:       
        calcScore *= 1.1    

    if resultScore:
        print(f"=> CALCUL RESULT : {calcScore:.3f}")
        print(f"=> PROMPT LENGTH : {promptLength}")
        print("=> IS CALC : True" if calcScore >= 0.5 else "=> IS CALC : False")

    if calcScore >= 0.5:
        return "calc"
    else:
        return "process"
        

