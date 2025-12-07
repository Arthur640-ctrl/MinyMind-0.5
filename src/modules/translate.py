import re
from googletrans import Translator as GoogleTranslator
import random

LANGS = {
    "anglais": "en",
    "angleterre": "en",
    "espagnol": "es",
    "français": "fr",
    "francais": "fr",
    "allemand": "de",
    "italien": "it",
    "japonais": "ja",
    "portugais": "pt",
    "arabe": "ar"
}

LANGS_NAMES = {v: k for k, v in LANGS.items()}

class TranslationRequest:
    def __init__(self, raw, text=None, dest=None):
        self.raw = raw
        self.text = text
        self.dest = dest

def find_language(sentence):
    s = sentence.lower()
    for k, v in LANGS.items():
        if k in s:
            return v
    return None

def find_text_to_translate(sentence):
    s = sentence.lower()
    
    # 1️⃣ Texte entre guillemets '...' ou "..."
    m = re.search(r"[\"'“”](.*?)[\"'“”]", sentence)
    if m:
        return m.group(1).strip()

    # 2️⃣ "Traduis bonjour en anglais"
    m = re.search(r"tradui[st]?\s+([a-zA-Z0-9éèêëàùûç ]+?)\s+en\s+[a-z]+", s)
    if m:
        return m.group(1).strip()

    # 3️⃣ "mot en langue" ou plusieurs mots
    m = re.search(r"(.+?)\s+en\s+([a-zA-Z]+)", sentence, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()

    return ""

def parse_translation(sentence):
    dest = find_language(sentence)
    text = find_text_to_translate(sentence)
    return TranslationRequest(sentence, text, dest)

class TranslatorModule:
    def __init__(self):
        self.translator = GoogleTranslator()
        self.responses = [
            "En <|dest|>, on dit <|src|> : <|result|>",
            "La traduction de '<|src|>' en <|dest|> est '<|result|>'.",
            "'<|src|>' se traduit par '<|result|>' en <|dest|>.",
            "En <|dest|>, on prononce '<|result|>' pour dire '<|src|>'.",
            "Si tu veux dire '<|src|>' en <|dest|>, tu peux dire '<|result|>'.",
            "Traduction en <|dest|> : '<|src|>' → '<|result|>'",
            "En <|dest|>, '<|src|>' devient '<|result|>'.",
            "'<|src|>' = '<|result|>' en <|dest|>.",
            "Voici comment on dit '<|src|>' en <|dest|> : '<|result|>'.",
            "Dans la langue <|dest|>, on utilise '<|result|>' pour '<|src|>'.",
            "Besoin de traduire '<|src|>' en <|dest|>? Ça donne '<|result|>'.",
            "En <|dest|>, le mot '<|src|>' correspond à '<|result|>'.",
            "'<|src|>' se dit '<|result|>' en <|dest|>, simple comme bonjour !",
            "Pour dire '<|src|>' en <|dest|>, il suffit de dire '<|result|>'.",
            "Traduction littérale : '<|src|>' → '<|result|>' en <|dest|>.",
            "On peut traduire '<|src|>' par '<|result|>' dans la langue <|dest|>.",
            "Dans <|dest|>, le terme pour '<|src|>' est '<|result|>'.",
            "'<|result|>' = '<|src|>' en <|dest|>, pratique non ?",
            "Voilà comment dire '<|src|>' en <|dest|> : '<|result|>'",
            "Traduction rapide : <|src|> → <|result|> (langue : <|dest|>)",
            "En résumé, '<|src|>' se dit '<|result|>' en <|dest|>.",
            "Tu veux dire '<|src|>' en <|dest|>? C'est '<|result|>'.",
            "Le mot '<|src|>' se traduit en <|dest|> par '<|result|>'.",
            "Petit tip linguistique : '<|src|>' = '<|result|>' en <|dest|>.",
            "À noter : en <|dest|>, '<|src|>' devient '<|result|>'.",
        ]

    def translate(self, text, dest):
        try:
            result = self.translator.translate(
                text,
                src="auto",
                dest=dest
            )

            if not result.text:
                return "[Traduction vide]"
            
            return {
                "src": text,
                "result": result.text,
                "dest": result.dest
            }
        
        except Exception as e:
            return f"[Erreur traduction] {e}"
    
    def reply(self, prompt):
        parsed = parse_translation(prompt)

        if not parsed.text or not parsed.dest:
            return "[Impossible de détecter texte ou langue cible]"
        
        data = self.translate(parsed.text, parsed.dest)

        template = random.choice(self.responses)

        output = template.replace("<|src|>", data["src"]) \
            .replace("<|dest|>", LANGS_NAMES[data["dest"]]) \
            .replace("<|result|>", data["result"])

        return output
        
