# This is where every transaction happens
# Where all the files and api connections flow


from fastapi import FastAPI,  File, UploadFile
import pytesseract
from PIL import Image
from groq import Groq
import io 
import os
import base64
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
async def extract_text(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    extracted_text = pytesseract.image_to_string(image)
    return {"extracted_text": extracted_text}

    print("Pre processing with OCR")
    await process_text("Hello")
    await access_groq()
    await groq_image_access()

async def process_text(input_text: str):

    print("Calling something else")

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
            "content": "I am sending you a png that contains handwritten text. Convert it to LaTeX.",
        }
    ],
    model=MODEL_NAME,
)
    print(chat_completion.choices[0].message.content)

    return chat_completion.choices[0].message.content

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

async def groq_image_access():
   image_path = "./src/test-images/test-1.png"
   base64_image = encode_image(image_path)
   client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
   chat_completion = client.chat.completions.create(
    model="llama-3.2-90b-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Return the LaTeX of this expression."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                }
            ],
        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)
   return chat_completion.choices[0].message.content
    # print(chat_completion.choices[0].message.content)
    # return(chat_completion.choices[0].message.content)



if __name__ == "__main__":
    access_groq()   




