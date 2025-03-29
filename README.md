### BlasterHacks 2025 Handwriting to Latex

## Before running anything, run this command inside the python virtual environment

`pip install -r install/requirements.txt `
To run:
uvicorn src.main:app --reload

to send things to the server:
curl -X POST http://127.0.0.1:8000/extract-text/
curl -X POST -F "file=@src/test-images/test-1.png" http://127.0.0.1:8000/extract-text/

## To run tests

`pytest src/tests.py -v`
