from ollama import chat
from ollama import ChatResponse


def ollama_chat(question):
    response: ChatResponse = chat(model='llama3.2:1b', messages=[
        {
            'role': 'user',
            'content': question,
        },
    ])
    # access fields directly from the response object
    return response.message.content
