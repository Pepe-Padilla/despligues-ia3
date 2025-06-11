from fastapi import FastAPI
#import os
#import google.generativeai as genai
#from dotenv import load_dotenv
from transformers import pipeline

app = FastAPI()

@app.get("/saluda")
def saluda():
    return {"Message":"Hell'o World!"}

@app.get('/generate')
def sentiment_classification(prompt: str):
    sentiment_pipeline = pipeline('sentiment-analysis')
    return {'Sentiment': sentiment_pipeline(prompt)[0]['label']}