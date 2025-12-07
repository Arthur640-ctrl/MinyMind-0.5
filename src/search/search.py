import json
import re
import random
import pickle
import numpy as np

class Searching:
    def __init__(self, prompt, light_word_weight = 0.5, heavy_word_weight = 1.0):
        self.prompt = prompt

        self.data_path = "data/qa.json"

        self.data = []

        with open(self.data_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

        self.stopwords = [".", ",", "!", ";", " ", "-", "_"]
        
        self.light_word_weight = 0.5
        self.heavy_word_weight = 1.0

        self.light_words = [
            "a","à","â","après","au","aux","autour","avant","avec","ce","cela","ces","cet","cette",
            "ci","comme","comment","dans","de","des","du","dedans","dehors","donc","dont","dos","dès",
            "elle","elles","en","encore","entre","et","eux","il","ils","je","la","le","les","leur",
            "lui","ma","mais","me","même","mes","moi","mon","ne","nos","notre","nous","on","ou","où",
            "par","parce","pas","pour","pourquoi","qu","que","quel","quelle","quelles","quels","qui",
            "sa","sans","se","sera","ses","si","sien","son","sont","sous","sur","ta","te","tes","toi",
            "ton","tous","tout","trop","très","tu","un","une","vos","votre","vous","y"
        ]

    def biased_random(self, x, y, bias=2.0):
        """
        Génère un nombre entre x et y avec plus de chance de tirer proche de y.
        
        bias > 1 : favorise Y
        bias < 1 : favorise X
        bias = 1 : uniforme
        """
        u = random.random()
        v = u ** (1 / bias)
        return x + (y - x) * v

    def cleaning(self, input):
        input = input.lower()
        sliced_input = re.findall(r'\w+|\s+|[^\w\s]', input)

        clean_input = []

        for world in sliced_input:
            if world in self.stopwords:
                continue
            else:
                clean_input.append(world)

        return clean_input

    def search(self, lenght_score_percent = 0.2, words_weight=True, debug=False):
        prompt = self.cleaning(self.prompt)
        data = self.data

        result = []

        for q in data:
            question = self.cleaning(q["Q"])
            
            score = 0

            for word in prompt:
                if word in question:
                    if words_weight:
                        if word in self.light_words:
                            score += self.light_word_weight
                        else:
                            score += self.heavy_word_weight
                    else:
                        score += 1

            max_len = max(len(prompt), len(question))
            diff_percent = abs(len(prompt) - len(question)) / max_len

            if diff_percent <= lenght_score_percent:
                score += 1
            
            result.append({
                "Q": q["Q"],
                "score": score
            })

        result = sorted(result, key=lambda x: x["score"], reverse=True)

        if debug:
            for i in result:
                print("Score : ", i["score"], " Question : ", i["Q"])

        return result

    def choice(self, questions, view = 10, debug=False):
        selected = []

        for i in range(view):
            selected.append(questions[i])

        selection_number = int(self.biased_random(view, 0, 10.0))

        if debug:
            print("Séléction : ", selected[selection_number]["Q"], " Number : ", selection_number)

        return selected[selection_number]["Q"]
