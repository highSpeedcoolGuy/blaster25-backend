import os 

from groq import Groq
from dotenv import load_dotenv


load_dotenv() 


MODEL_NAME = "llama-3.2-90b-vision-preview"

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def groq_query():
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model=MODEL_NAME,
)
    print(chat_completion.choices[0].message.content)

    return 0; 

# if __name__ == "__main__":
#     groq_query()

