
from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama3.2:1b', messages=[
  {
    'role': 'user',
    'content': 'is serbia in the eu',
  },
])
# access fields directly from the response object
print(response.message.content)