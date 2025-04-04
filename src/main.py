# This is where every transaction happens
# Where all the files and api connections flow


from fastapi import FastAPI,  File, UploadFile
import pytesseract
from PIL import Image
from groq import Groq
import io 
import os
import openai
import base64
import pprint
import asyncio
# from groqing import groq_query
from dotenv import load_dotenv
load_dotenv() 

app = FastAPI()


def parse_latex(latex_text):
    return latex_text.split("```latex")[1].split("```")[0]


MODEL_NAME = "llama-3.2-90b-vision-preview"


@app.get("/")
def read_root():
    return {"message": "FASTApi"}


@app.get("")


# Takes png and outputs text and ? images
@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    #image = Image.open(io.BytesIO(await file.read()))
    #extracted_text = pytesseract.image_to_string(image)
    
    print("Pre processing with OCR")
    await process_text("Hello")
    return_val = await access_groq()

    return {"extracted_text": return_val}
    # await groq_image_access()


async def process_text(input_text: str):

    print("Calling something else")
with open('/Users/ajmendes/backend/uploads/prompt.txt', 'r') as f:
    prompt_content = f.read()


prompt = f"""
You must return all the LaTeX code for the given image provided. Output all of the code. 

#Important Rules: 
You MUST start your latex code with ```latex and end with ```. 
You must include 
\documentclass{{article}}
\begin{{document}}
The User's prompt is as follows:
""" + prompt_content


async def access_groq(image_path="./src/test-images/test-1.png"):
    print("Made it to access_groq")
    # image_path = "./src/test-images/test-1.png"
    base64_image = encode_image(image_path)
    client = openai.OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=os.environ.get("GROQ_API_KEY")    
    )
    # client = openai.OpenAI()
    # os.environ.get("GROQ_API_KEY")
    # print(f"API Key: {x}")
    # print("Accessing Groq")
    completion = client.chat.completions.create( 
        model=MODEL_NAME,
        # model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
    )
    # pprint.pp(parse_latex(completion.choices[0].message.content))
    print(parse_latex(completion.choices[0].message.content))

    return (parse_latex(completion.choices[0].message.content))


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
   
   print(chat_completion.choices[0].message.content)
   return chat_completion.choices[0].message.content
    # print(chat_completion.choices[0].message.content)
    # return(chat_completion.choices[0].message.content)


loop = asyncio.get_event_loop()
loop.run_until_complete(access_groq('/Users/ajmendes/backend/uploads/test_file.png'))
# if __name__ == "__main__":
#     access_groq()   




