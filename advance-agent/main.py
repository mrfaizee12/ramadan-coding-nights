import os  # For accessing environment variables
import chainlit as cl  # type: ignore # Web UI framework for chat applications
from dotenv import load_dotenv  # For loading environment variables
from typing import Optional, Dict  # Type hints for better code clarity
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel  # type: ignore

# Load environment variables from .env file
load_dotenv()

# Get Gemini API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize OpenAI provider with Gemini API settings
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

# Configure the language model
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)

agent = Agent(
    name="Greeting Agent",
    instructions="""You are a Greeting Agent designed to provide friendly interactions and information about Faizee.

Your responsibilities:
1. Greet users warmly when they say hello (respond with 'Salam from Faizee').
2. Say goodbye appropriately when users leave (respond with 'Allah Hafiz from Faizee').
3. When users ask for information about Faizee, reply with: 'Information about Faizee is not available at the moment.'
4. When users ask about cricket or weather, provide appropriate and helpful answers based on your knowledge.
5. When users ask about programming topics:
   - If the question is about Python, provide detailed and helpful answers.
   - If the question is about any other programming language (e.g., TypeScript, JavaScript, etc.), reply with: 'Sorry, I can only provide programming information about Python.'
6. For any other questions not related to greetings, Faizee, cricket, weather, or Python programming, politely explain: 'I'm only able to provide greetings and information about Faizee. I can't answer other questions at this time.'

Always maintain a friendly, professional tone and ensure responses are helpful within your defined scope.""",
    model=model,
    # No external API tool is used now.
)

# Decorator to handle OAuth callback from GitHub
@cl.oauth_callback
def oauth_callback(
    provider_id: str,  # ID of the OAuth provider (GitHub)
    token: str,  # OAuth access token
    raw_user_data: Dict[str, str],  # User data from GitHub
    default_user: cl.User,  # Default user object from Chainlit
) -> Optional[cl.User]:  # Return User object or None
    """
    Handle the OAuth callback from GitHub.
    Return the user object if authentication is successful, None otherwise.
    """
    print(f"Provider: {provider_id}")  # Debugging: Print provider ID
    print(f"User data: {raw_user_data}")  # Debugging: Print user data
    return default_user  # Return the default user object

# Handler for when a new chat session starts
@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])  # Initialize empty chat history
    await cl.Message(
        content="Hello! How can I help you today?"
    ).send()  # Send welcome message

# Handler for incoming chat messages
@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")  # Get chat history from session
    history.append({"role": "user", "content": message.content})  # Add user message to history

    result = await cl.make_async(Runner.run_sync)(agent, input=history)
    response_text = result.final_output

    await cl.Message(content=response_text).send()
    history.append({"role": "assistant", "content": response_text})
    cl.user_session.set("history", history)
