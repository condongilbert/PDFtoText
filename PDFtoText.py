import pdfplumber
import pytesseract
from PIL import Image

# Open the PDF file
with pdfplumber.open('WallyBook.pdf') as pdf:
    # Open a text file to write the extracted text
    with open('output.txt', 'w') as output_file:
        for page_number, page in enumerate(pdf.pages, start=1):
            # Try to extract text using pdfplumber
            text = page.extract_text()
            if text:
                output_file.write(f"Page {page_number}:\n{text}\n\n")
            else:
                # If no text is found, perform OCR
                output_file.write(f"Page {page_number} (OCR):\n")
                image = page.to_image(resolution=300).original  # Convert page to image
                ocr_text = pytesseract.image_to_string(Image.fromarray(image))
                output_file.write(f"{ocr_text}\n\n")