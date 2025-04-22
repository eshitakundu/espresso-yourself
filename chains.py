from langchain.chains import LLMChain
from langchain_google_genai import GoogleGenerativeAI
from prompts import CHARACTER_PROMPTS
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# More flexible LLM configuration
def get_llm(temperature=0.7, max_tokens=150):
    return GoogleGenerativeAI(
        model="models/gemini-1.5-pro-latest",
        temperature=temperature,
        max_tokens=max_tokens
    )

def get_chain(character: str, memory, temperature=0.7):

    prompt = CHARACTER_PROMPTS[character]
    if character == "Customer":
        temperature = min(0.9, temperature + 0.1)
    
    llm = get_llm(temperature=temperature)
    
    return LLMChain(
        llm=llm,
        prompt=prompt,
        memory=memory,
        output_key="text",  
        verbose=False
    )
