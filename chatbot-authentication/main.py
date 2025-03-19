import os  # OS module ko import kar rahe hain taake environment variables access kar sakein
import chainlit as cl  # type: ignore # Chainlit ko import kar rahe hain taake chatbot interface ban sake
import google.generativeai as genai  # Google Generative AI ko import kar rahe hain Gemini API ke liye
from dotenv import load_dotenv  # Dotenv ko import kar rahe hain taake .env file se environment variables load ho sakein
from typing import Optional, Any, Dict  # Type hints ke liye Optional, Any, aur Dict import kar rahe hain

# .env file se environment variables load kar rahe hain
load_dotenv()  

# Gemini API key environment variable se fetch kar rahe hain
gemini_api_key = os.getenv("GEMINI_API_KEY")  

# Gemini AI model ke liye API key configure kar rahe hain
genai.configure(api_key=gemini_api_key)  

# Gemini 2.0 Flash model initialize kar rahe hain
model = genai.GenerativeModel(model_name="gemini-2.0-flash")  

# OAuth authentication ke liye callback function define kar rahe hain
@cl.oauth_callback  
def oauth_callback(
    provider_id: str,  # Authentication provider ka naam (e.g., GitHub)
    token: str,  # Authentication ke liye access token
    raw_user_data: Dict[str, Any],  # User ka raw authentication data
    default_user: cl.User,  # Default user object jo authentication ke baad return hoga
) -> Optional[cl.User]:  

    # Provider ID ko print kar rahe hain (e.g., "github")
    print(f"Provider: {provider_id}")  

    # User ka authentication data print kar rahe hain
    print(f"User data: {raw_user_data}")  

    # Default authenticated user return kar rahe hain
    return default_user  

# Jab naya chat session start hota hai, yeh function chalega
@cl.on_chat_start  
async def handle_chat_start():  

    # User session me ek khali chat history initialize kar rahe hain
    cl.user_session.set("history", [])  

    # Chatbot ka welcome message bhej rahe hain
    await cl.Message(content="Hello! How can I help you today?").send()  

# Jab user koi message bhejta hai, yeh function chalega
@cl.on_message
async def handle_message(message: cl.Message):  

    # Pehle se stored chat history retrieve kar rahe hain
    history = cl.user_session.get("history")  
    
    # User ka naya message history me add kar rahe hain
    history.append({"role": "user", "content": message.content})

    # Model ke liye formatted history banane ke liye ek empty list
    formatted_history = []
    
    # Chat history ke har message ko loop me format kar rahe hain
    for msg in history:
        # Message sender ka role set kar rahe hain (user ya model)
        role = "user" if msg["role"] == "user" else "model"

        # Formatted message list me add kar rahe hain
        formatted_history.append({"role": role, "parts":[{"text": msg["content"]}]})

    # Gemini AI model ko formatted history bhej rahe hain aur response generate kar rahe hain
    response = model.generate_content(formatted_history)

    # AI model ka response text extract kar rahe hain
    response_text = response.text if hasattr(response, "text") else ""

    # AI assistant ka response history me add kar rahe hain
    history.append({"role": "assistant", "content": response_text})
    
    # Updated history ko user session me save kar rahe hain
    cl.user_session.set("history", history)

    # AI assistant ka response user ko bhej rahe hain
    await cl.Message(content=response_text).send()
