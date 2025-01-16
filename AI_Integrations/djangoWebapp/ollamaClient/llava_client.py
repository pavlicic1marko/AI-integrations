import ollama

res = ollama.chat(
	model="llava:7b",
	messages=[
		{
			'role': 'user',
			'content': 'Describe this image:',
			'images': ['./UN.jpg']
		}
	]
)

print(res['message']['content'])