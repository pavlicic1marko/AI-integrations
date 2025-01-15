import os
import openai
from dotenv import load_dotenv

#load and set api_key for open ai
load_dotenv()
api_key = os.getenv("chat_gpt_api_key")
openai.api_key = api_key

# model options
#gpt_4 = "gpt-4"
#gpt_3x5_turbo = "gpt-3.5-turbo"

def ask_chat_gpt(question, model):
    # Initial message to ask the first question
    messages = [{"role": "user", "content": question}]

    # Call the API
    completion = openai.chat.completions.create(model=model, messages=messages)

    # Print the answer we received for the 1st question
    return completion.choices[0].message.content


if __name__ == "__main__":
    ask_chat_gpt("is serbia a member of the eu")