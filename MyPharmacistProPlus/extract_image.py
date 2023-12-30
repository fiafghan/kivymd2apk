import pytesseract
from PIL import Image

# Extract text from the image
def extract_text_from_image(image_path):
    # Load the image
    image = Image.open(image_path)

    # Extract text from the image
    text = pytesseract.image_to_string(image)
    return text