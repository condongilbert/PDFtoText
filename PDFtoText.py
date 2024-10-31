import fitz  # PyMuPDF
import os

# Path to the PDF file
pdf_path = 'WallyBook.pdf'  # Replace with your PDF file path
print(f"Loading PDF from: {os.path.abspath(pdf_path)}")

try:
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    print(f"Opened PDF with {pdf_document.page_count} pages.")
    
    # Initialize a list to store the extracted text
    extracted_text = []

    # Iterate through each page and extract text
    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        text = page.get_text()
        extracted_text.append(text)
        print(f"Extracted text from page {page_number + 1}")

    # Combine all extracted text into a single string
    all_text = "\n".join(extracted_text)

    # Save the extracted text to a .txt file
    output_file = 'extracted_text.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(all_text)
    
    print(f"Extracted text saved to: {os.path.abspath(output_file)}")

except Exception as e:
    print(f"Error processing PDF: {e}")