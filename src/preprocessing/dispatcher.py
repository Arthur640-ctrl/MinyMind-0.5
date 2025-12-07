import re
import json
from sentence_transformers import SentenceTransformer, util

train_data_embeddings = None
train_data = None

model = None

def init():
    global train_data, train_data_embeddings, model

    model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

    with open("data/dispatcher.json", "r", encoding="utf-8") as f:
        train_data = json.load(f)
    
    train_data_embeddings = {cat: model.encode(sentences) for cat, sentences in train_data.items()}

def detect_intent_st(sentence):
    emb = model.encode(sentence)
    scores = {}
    for cat, emb_list in train_data_embeddings.items():
        sims = [util.cos_sim(emb, e).item() for e in emb_list]
        scores[cat] = max(sims)
    return max(scores, key=scores.get)

def dispatch(prompt, calcResultDebug = False, resultScore = False, finalChoice = False):
    return detect_intent_st(prompt)

    
    
        

