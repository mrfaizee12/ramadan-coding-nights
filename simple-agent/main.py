import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel # type: ignore

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

agent = Agent(
    name="Greetings Agent",
    instructions="You are a Greetings Agent, Your task is to greet the user with a friendly message, when someone says hi or hello you've reply back with Assalamoalaikum from Faizan, if someone says bye then say allah hafiz from Faizan Anjum, when someone asks other than greeting then say Faizan is here just for greeting, I can't answer other than greeting, sorry for that.",
    model=model
)

user_question = input("Enter your question: ")

result = Runner.run_sync(agent, user_question)
print(result.final_output)