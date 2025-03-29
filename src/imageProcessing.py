import pytesseract
from pytesseract import Output
from PIL import Image
import numpy as np
import cv2

# Load image
image = cv2.imread('../data/test.png')
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get detailed OCR results including confidence
results = pytesseract.image_to_data(rgb_image, output_type = Output.DICT)

# Set confidence threshold
confidence_threshold = 60  # Adjust this value based on your needs

uncertain_regions = []
n_boxes = len(results['text'])

for i in range(n_boxes):
    if int(results['conf'][i]) < confidence_threshold and results['text'][i].strip() != '':
        # Get coordinates of uncertain text
        x = results['left'][i]
        y = results['top'][i]
        w = results['width'][i]
        h = results['height'][i]
        
        # Extract the uncertain region
        uncertain_region = rgb_image[y:y+h, x:x+w]
        uncertain_regions.append({
            'region': uncertain_region,
            'confidence': results['conf'][i],
            'text': results['text'][i],
            'coordinates': (x, y, w, h)
        })
        
        # Draw rectangle around uncertain text (for visualization)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
python-multipart
cv2.imwrite('uncertain_regions.png', image)

# Print results
for i, region in enumerate(uncertain_regions):
    print(f"Uncertain region {i+1}:")
    print(f"  Attempted text: '{region['text']}'")
    print(f"  Confidence: {region['confidence']}")
    print(f"  Coordinates: {region['coordinates']}")
    
    # Save each uncertain region as a separate image
    region_img = Image.fromarray(region['region'])
    region_img.save(f"uncertain_region_{i+1}.png")