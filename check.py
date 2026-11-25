import os
from dotenv import load_dotenv
from google import genai
# load from .env
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# check each model in the list of Gemini models
for model in client.models.list():
    if "generateContent" in (model.supported_actions or []):
        print(model.name)