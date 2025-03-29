import cv2
import pytesseract
import sympy as sp

# Set Tesseract OCR path (if needed)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    """Preprocess the image for better OCR accuracy."""
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    return img

def extract_text_from_image(image_path):
    """Extracts text from an image using pytesseract."""
    img = preprocess_image(image_path)
    text = pytesseract.image_to_string(img, config="--psm 6")
    return text

def solve_math_expression(expression):
    """Solves a math problem using sympy."""
    try:
        # Convert the extracted text into a sympy equation
        lhs, rhs = expression.split("=")  # Handle equations
        solution = sp.solve(sp.sympify(lhs) - sp.sympify(rhs))
        return solution
    except Exception as e:
        return f"Error solving equation: {e}"

# Example usage
image_path = "test-images/limits.png"
extracted_text = extract_text_from_image(image_path)
print("Extracted Text:", extracted_text)

# Try solving the extracted expression
solution = solve_math_expression(extracted_text)
print("Solution:", solution)
