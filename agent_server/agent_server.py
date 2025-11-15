
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from google import generativeai as genai

API_KEY = os.environ.get("GOOGLE_API_KEY", "")
if not API_KEY:
    raise ValueError("Missing GOOGLE_API_KEY environment variable. Set it before running.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])

class Query(BaseModel):
    message: str

@app.post("/chat")
def chat(data: Query):
    prompt = f"You are an AI model expert. Explain clearly: {data.message}"
    out = model.generate_content(prompt)
    return {"reply": out.text}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
