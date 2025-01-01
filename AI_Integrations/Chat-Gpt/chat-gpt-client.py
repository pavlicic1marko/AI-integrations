from dotenv import load_dotenv
import os
import openai

load_dotenv()

api_key = os.getenv("chat_gpt_api")
openai.api_key = api_key

# model options
gpt_4 = "gpt-4"
gpt_3x5_turbo = "gpt-3.5-turbo"


def ask_chat_gpt_a_question(question):
    model_id = gpt_4
    # Initial message to ask the first question
    messages = [{"role": "user", "content": question}]

    # Call the API
    completion = openai.chat.completions.create(model=model_id, messages=messages)

    # Print the answer we received for the 1st question
    print(completion.choices[0].message.content)

if __name__ == "__main__":
    ask_chat_gpt_a_question("is Serbia in the EU")