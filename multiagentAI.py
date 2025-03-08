import asyncio
import os

from browser_use.agent.service import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

async def agent_task(task_description):
    """Creates and runs an AI agent for a given task."""
    api_key = os.getenv("GEMINI_API_KEY", "AIzaSyCERo_dB9vo_AQ0bW8SZlMC5UK6izAljuI")
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))
    agent = Agent(task_description, llm, use_vision=True)
    history = await agent.run()
    return history.final_result()

async def site_validation():
    """Executes AI agents in a structured sequence for reliable UI testing."""
    os.environ["GEMINI_API_KEY"] = "AIzaSyCERo_dB9vo_AQ0bW8SZlMC5UK6izAljuI"

    agent1_task = (
        "UI Automation Tester: Open website https://www.saucedemo.com/ and login "
        "using credentials displayed on the page. After login, select the first 2 "
        "products and add them to the cart. Confirm task completion."
    )
    agent1_result = await agent_task(agent1_task)
    print("Agent 1 Result:", agent1_result)

    agent2_task = (
        "UI Automation Tester: After cart confirmation, proceed to checkout, "
        "place the order, and verify that the thank-you message is displayed."
    )
    agent2_result = await agent_task(agent2_task)
    print("Agent 2 Result:", agent2_result)

async def main():
    await site_validation()

if __name__ == "__main__":
    asyncio.run(main())