import os  # Importing os to access environment variables
import chainlit as cl  # Importing Chainlit for building the chatbot interface
import google.generativeai as genai  # Importing Google Generative AI for Gemini API
from dotenv import load_dotenv  # Importing dotenv to load environment variables

load_dotenv()  # Loading environment variables from the .env file

gemini_api_key = os.getenv("GEMINI_API_KEY")  # Retrieving the Gemini API key from environment variables

genai.configure(api_key=gemini_api_key)  # Configuring the generative AI model with the API key

model = genai.GenerativeModel(model_name="gemini-2.0-flash")  # Initializing the Gemini model

@cl.on_chat_start  # Defining an event that triggers when the chat starts
async def handle_chat_start():
    await cl.Message(content="Hello! How can I help you today?").send()  # Sending a welcome message

@cl.on_message  # Defining an event that triggers when a user sends a message
async def handle_message(message: cl.Message):
    prompt = message.content  # Storing the user message in the 'prompt' variable

    response = model.generate_content(prompt)  # Generating AI response using the Gemini model

    response_text = response.text if hasattr(response, "text") else ""  # Extracting the text from the response

    await cl.Message(content=response_text).send()  # Sending the AI-generated response back to the user
