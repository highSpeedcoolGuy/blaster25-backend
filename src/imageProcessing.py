import pytesseract
from pytesseract import Output
from PIL import Image
import numpy as np
import cv2

# Load image
image = cv2.imread('/home/jabuan/BlasterHacks/backend/src/test-images/test.png')
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get detailed OCR results including confidence
results = pytesseract.image_to_data(rgb_image, output_type=Output.DICT)

# Set confidence threshold
confidence_threshold = 100 # Adjust this value based on your needs

uncertain_regions = []
certain_text = []
n_boxes = len(results['text'])

for i in range(n_boxes):
    # Skip empty text
    if results['text'][i].strip() == '':
        continue
        
    # Check confidence level
    if int(float(results['conf'][i])) < confidence_threshold:
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
    else:
        # Store text with high confidence
        certain_text.append(results['text'][i])

# Save visualization image
cv2.imwrite('uncertain_regions.png', image)

# Write recognized text to a file
with open('recognized_text.txt', 'w') as text_file:
    # Write the certain text
    text_file.write("RECOGNIZED TEXT (HIGH CONFIDENCE):\n")
    text_file.write("---------------------------------\n")
    text_file.write(" ".join(certain_text))
    text_file.write("\n\n")
    
    # Write information about uncertain regions
    text_file.write("UNCERTAIN REGIONS:\n")
    text_file.write("-----------------\n")
    for i, region in enumerate(uncertain_regions):
        text_file.write(f"Region {i+1}:\n")
        text_file.write(f"  Attempted text: '{region['text']}'\n")
        text_file.write(f"  Confidence: {region['confidence']}\n")
        text_file.write(f"  Coordinates: {region['coordinates']}\n")
        text_file.write("\n")

# Print results
print(f"Found {len(uncertain_regions)} uncertain regions and {len(certain_text)} certain words")
print(f"Results saved to 'recognized_text.txt'")

# Save each uncertain region as a separate image
for i, region in enumerate(uncertain_regions):
    region_img = Image.fromarray(region['region'])
    region_img.save(f"uncertain_region_{i+1}.png")