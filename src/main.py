# This is where every transaction happens
# Where all the files and api connections flow


from fastapi import FastAPI, File, UploadFile
import pytesseract
from PIL import Image
import io 
import groq

app = FastAPI()

GROQ_API_KEY = "Nothing yet!"
client = groq.Client(api_key = GROQ_API_KEY)


@app.get("/")
def read_root():
    return{"message": "FASTApi"}

@app.get("")

#Takes png and outputs text and ? images
async def extract_text(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    extracted_text = pytesseract.image_to_string(image)
    return {"extracted_text": extracted_text}

#Groq processing right here
# async def process_test(input_text: str):
#     response = client.chat.completions.create()
#     print("Calling groq")
