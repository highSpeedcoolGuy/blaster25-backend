# This is where every transaction happens
# Where all the files and api connections flow


from fastapi import FastAPI,  UploadFile
import pytesseract
from PIL import Image
from groq import Groq
import io 
import os
# from groqing import groq_query
from dotenv import load_dotenv
load_dotenv() 

app = FastAPI()



MODEL_NAME = "llama-3.2-90b-vision-preview"

@app.get("/")
def read_root():
    return{"message": "FASTApi"}

@app.get("")

#Takes png and outputs text and ? images
@app.post("/extract-text/")
async def extract_text():

    print("Pre processing with OCR")
    await process_test("Hello")
    await access_groq()

async def process_test(input_text: str):

    print("Calling something")

async def access_groq():
    client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
    x = os.environ.get("GROQ_API_KEY")
    # print(f"API Key: {x}")
    # print("Accessing Groq")
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

    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    access_groq()   




