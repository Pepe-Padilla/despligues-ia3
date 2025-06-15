from fastapi import FastAPI
#import os
#import google.generativeai as genai
#from dotenv import load_dotenv
from transformers import pipeline
from . import utils as ut

app = FastAPI()

@app.get("/factorial")
def factorial(n: int):
    return {"result":ut.factorial(n)}

@app.get("/cammelCase")
def cammelCase(variable:str):
    return {"result":ut.cammelCase(variable)}

@app.post("/order")
def newPassword(order: ut.Execution):
    return ut.order(order)

@app.get('/classification')
def text_classification(query: str):
    pipe = pipeline('text-classification')
    return {'classification': pipe(query)[0]['label']}


@app.get("/translateES2EN")
def translate(query:str):
    pipe = pipeline("text-generation", model="sarvamai/sarvam-translate")
    messages = [
        {"role": "system", "content": f"Translate the text below to English."},
        {"role": "user", "content": query}
    ]
    print(messages)
    respuesta = pipe(messages)
    try:
        generated_text = respuesta[0]["generated_text"]
        for content in generated_text:
            if content["role"] == "assistant":
                return {"content": content["content"]}
    except:
        print(respuesta)
    
    return respuesta