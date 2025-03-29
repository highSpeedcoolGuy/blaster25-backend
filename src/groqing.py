import os 

from groq import Groq
from dotenv import load_dotenv

client = Groq( 
    api_key = os.environ.get("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")
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Helpful assistant"
        },
        {
            "role": "user",
            "content": "Explain the importance of something"
        }

    ],
    model = "llama-3.3-70b-versatile",
    
)
print(chat_completion.choices[0].message.content)