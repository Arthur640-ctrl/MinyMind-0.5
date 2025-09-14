from preprocessing.preprocesser import preprocess
from preprocessing.dispatcher import dispatch
from embeddings.search import Searching
from generation.reponse import Response

def process(rawPrompt):
    prompt = preprocess(rawPrompt)

    dispatchResult = dispatch(prompt, False, False, False)

    if dispatchResult == "process":
        search = Searching(prompt)
        questions = search.search(False)
        question = search.choice(questions)

        responseClass = Response(question)

        response = responseClass.reply()
        print(response)

    return prompt

while True:
    prompt = input("User > ")
    
    if prompt.lower() == "quit":
        break
    else:
        process(prompt)
