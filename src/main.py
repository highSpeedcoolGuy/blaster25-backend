# This is where every transaction happens
# Where all the files and api connections flow


from fastapi import FASTAPI, FILE, UploadFile
import pytesseract
from PIL import Image
import io 
import groqing

app = FastAPI()

GROQ_API_KEY = "Nothing yet!"
client = groq.Client(api_key = GROQ_API_KEY)


@app.get("/")
def read_root():
    return{"message": "FASTApi"}

@app.get("")

#Takes png and outputs text and ? images
async def extract_text():

    print("Pre processing with OCR")

async def process_test(input_text: str):

    print("Calling groq")


while(true):
    break