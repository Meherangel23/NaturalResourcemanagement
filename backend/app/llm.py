import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GOOGLE_API_KEY")
# Optionally allow overriding the model via env var `LLM_MODEL`.
preferred_model = os.environ.get("LLM_MODEL")

model = None

if not api_key:
    print("ERROR: GOOGLE_API_KEY environment variable not set.")
    print("Please create a .env file in the backend directory and add your API key.")
else:
    try:
        genai.configure(api_key=api_key)
    except Exception as e:
        print(f"Error configuring Generative AI client: {e}")

def list_available_models():
    """Return a list of model ids available to the configured API key."""
    try:
        models = genai.list_models()
        ids = [m.name for m in models]
        print("Available models:")
        for mid in ids:
            print(" -", mid)
        return ids
    except Exception as e:
        print(f"Could not list models: {e}")
        return []


def get_chatbot_reply(message: str):
    """
    Sends the user's message to the Gemini model and returns the response.
    """
    global model

    if not api_key:
        return "I'm sorry, the chatbot is not configured correctly (missing API key)."

    if model is None:
        model_id = preferred_model or "gemini-1.5-flash-latest"
        try:
            model = genai.GenerativeModel(model_id)
            print(f"Using model: {model_id}")
        except Exception as e:
            print(f"Could not instantiate GenerativeModel('{model_id}'): {e}")
            return "I'm sorry, no AI model is currently available. Please check server logs."

    try:
        response = model.generate_content(message)
        return response.text
    except Exception as e:
        print(f"Unexpected error when generating reply: {e}")
        return "I'm sorry, an unexpected error occurred while generating a reply."


if __name__ == "__main__":
    # Quick CLI for debugging: list available models and try a short sample.
    print("Running llm.py self-test")
    models = list_available_models()
    print("Models discovered:", models)
    sample = "Hello, what's the weather like today?"
    reply = get_chatbot_reply(sample)
    print("Sample reply:", reply)