import json
import random

class Response:
    def __init__(self, question):
        self.question = question
    
    def reply(self):
        with open("data/qa.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        answers = []
        
        for pair in data:
            if pair["Q"] == self.question:
                answers = pair["A"]

                return random.choice(answers)