from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

def get_model(model_name: str):
    model_name = model_name.lower()
    model_map = {
        "qwen": "Qwen-Qwen-32B",
        "llama3": "LLaMA3-70B",
        "llama2": "LLaMA2-70B",
        "mixtral": "Mixtral-8x7B",
        "gemma": "Gemma-7B",
        "deepseek": "DeepSeek-Coder-33B"
    }

    if model_name not in model_map:
        raise ValueError(f"Unsupported model: {model_name}")

    return ChatGroq(model=model_map[model_name], api_key=groq_api_key)
