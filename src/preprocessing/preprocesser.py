import re

stopwords = [".", "?", ",", "!", ";"]

def preprocess(prompt, ):
    # Mettre le prompt en minuscule
    promptLower = prompt.lower()
    # Slice word
    promptSlice = re.findall(r"\b\w+\b", promptLower)
    # Remove ponctuation
    promptSlice = [word for word in promptSlice if word not in stopwords]

    promptClean = " ".join(promptSlice)

    return promptClean



