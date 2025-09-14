import json
from sentence_transformers import SentenceTransformer, util
import re
import random

stopwords = [".", "?", ",", "!", ";"]

class Searching:
    def __init__(self, prompt, modelName = 'paraphrase-multilingual-MiniLM-L12-v2'):
        self.prompt = prompt
        self.modelName = modelName
        self.model = SentenceTransformer(self.modelName)

    def cleaning(self, prompt):
        promptLower = prompt.lower()
        promptSlice = re.findall(r"\b\w+\b", promptLower)
        promptSlice = [word for word in promptSlice if word not in stopwords]

        promptClean = " ".join(promptSlice)

        return promptClean

    def search(self, debug):
        promptEmbeding = self.model.encode(self.prompt, convert_to_tensor=True)

        data = []
        selected = []

        with open("data/qa.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        for pair in data:
            question = self.cleaning(pair["Q"])
            questionEmbeding = self.model.encode(question, convert_to_tensor=True)

            similarity = util.cos_sim(questionEmbeding, promptEmbeding).item()

            if similarity >= 0.5:
                selected.append({
                    "q": pair["Q"],
                    "result": similarity
                })

        if debug:
            top5 = sorted(selected, key=lambda x: x["result"], reverse=True)[:5]

            for result in top5:
                print(f'| Sentence : {result["q"]} => {result["result"]}')

        return selected

    def choice(self, questions, minimumThreshold=0.7, originality=0.2, debug = False):
        candidates = []

        for sentence in questions:
            if sentence["result"] >= minimumThreshold:
                candidates.append(sentence)

        if not candidates:
            return None

        if debug:
            print("=== Scores avant pondération ===")
            for sentence in candidates:
                print(f'| {sentence["q"]} => {sentence["result"]}')

        for sentence in candidates:
            randomFactor = random.uniform(0, originality)
            weightedScore = sentence["result"] * (1 - randomFactor)
            sentence["result"] = weightedScore

        if debug:
            print("=== Scores après pondération ===")
            sortedData = sorted(candidates, key=lambda x: x["result"], reverse=True)
            for result in sortedData:
                print(f'| {result["q"]} => {result["result"]}')

        return candidates[0]["q"]