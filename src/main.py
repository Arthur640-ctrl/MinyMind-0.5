from fastapi import FastAPI, HTTPException, Depends, status, Response, Request
from pydantic import BaseModel
from preprocessing.dispatcher import dispatch, init
from search.search import Searching
from generation.reponse import Response
from modules.translate import TranslatorModule
import uvicorn

init()  # initialisation existante

app = FastAPI(title="MinyMind API")

# modèle de requête
class PromptRequest(BaseModel):
    prompt: str
    token: str

# endpoint principal
@app.post("/chat")
async def process_prompt(request: PromptRequest):

    if request.token != "abc123":
        raise HTTPException(status_code=401, detail="Non autorisé !")

    prompt = request.prompt
    dispatchResult = dispatch(prompt, False, False, False)

    if dispatchResult == "other":
        search = Searching(prompt)
        questions = search.search(False)
        question = search.choice(questions)

        responseClass = Response(question)
        response = responseClass.reply()
        
    elif dispatchResult == "traduction":
        trans = TranslatorModule()
        response = trans.reply(prompt)

    else:
        response = "[Aucune action correspondante]"

    errors = [
        "[Aucune action correspondante]",
        "[Impossible de détecter texte ou langue cible]",
        "[Traduction vide]"
    ]

    if response in errors:
        response = "Une petite erreur est survenue, n'hesites pas à la signaler pour permettre de m'améliorer. Je suis Tyrel 0.5 à ton service !" 

    return {"prompt": prompt, "response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000, log_level="info")