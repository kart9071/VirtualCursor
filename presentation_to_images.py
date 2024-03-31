from pdf2image import convert_from_path
from PIL import Image

def pdf_to_images(pdf_file, output_folder):
    images = convert_from_path(pdf_file)
    
    for i, image in enumerate(images):
        # Resize the image to 1280x720 pixels
        image = image.resize((1280, 720))
        
        image_path = f"{output_folder}/page_{i+1}.png"
        image.save(image_path, "PNG")
        print(f"Page {i+1} converted to {image_path}")

# Usage
pdf_file = "presentation.pdf"
output_folder = "Presentation"
pdf_to_images(pdf_file, output_folder)
