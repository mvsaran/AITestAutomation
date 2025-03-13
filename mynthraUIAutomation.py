import asyncio
import os

from browser_use.agent.service import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

async def MyntraAutomation():
    os.environ["GEMINI_API_KEY"] = "AIzaSyCizAljuI"  # Replace with your API key
    task = (
        'Important: I am a UI Automation tester performing a detailed test on Myntra.'
        '1. Launch the website https://www.myntra.com/.'
        '2. Select the "MEN" category from the top navigation bar.'
        '3. In the "Topwear" section, carefully locate and click on "Jackets".'
        '4. A new browser tab or window will open. Focus on this new tab/window.'
        '5. Identify the first product displayed in the product list. Click on this product to open its detailed page.'
        '6. **On the product detail page, look for a section labeled "Select Size" or a group of clickable buttons representing sizes.**'
        '7. **Within the size selection area, visually search for a button or label that clearly displays the letter "L". Click on this "L" size option.**'
        '8. Find the "Add to Bag" button and click it.'
        '9. Navigate to the shopping bag/cart.'
        '10. Verify that the product quantity, size (L), and product name in the bag exactly match the product you selected.'
        '11. Print a detailed verification result, including the product name, size, and quantity, and whether the verification was successful.'
    )
    api_Key = os.environ["GEMINI_API_KEY"]
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_Key))
    agent = Agent(task, llm, use_vision=True)
    history = await agent.run()
    test_result = history.final_result()
    print(test_result)

async def main():
    await MyntraAutomation()

if __name__ == "__main__":
    asyncio.run(main())
