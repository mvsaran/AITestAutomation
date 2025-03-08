import asyncio
import os

from browser_use.agent.service import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

async def SiteValidation():
    os.environ["GEMINI_API_KEY"] = "AIzaSyCERo_dB9vo_AQ0bW8SZlMC5UK6izAljuI"
    task = (
        'Important : Iam UI Automation tester validating the tasks'
        'Open website https://www.saucedemo.com/'
        'Login with username and password.login details are available in the same page'
        'After login, select first 2 products and add them to cart'
        'Then Checkout and place order'
        'verify thankyou message is displayed'
    )
    api_Key = os.environ["GEMINI_API_KEY"]
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_Key))
    agent = Agent(task, llm, use_vision=True)
    history = await agent.run()
    test_result = history.final_result()
    print(test_result)

async def main():
    await SiteValidation()

if __name__ == "__main__":
    asyncio.run(main())