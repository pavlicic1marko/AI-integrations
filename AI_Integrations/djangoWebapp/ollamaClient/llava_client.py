import ollama


def describe_image():
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

    return res['message']['content']
