import pdfplumber

# Open the PDF file
with pdfplumber.open('PO101023997.pdf') as pdf:
    # Open a text file to write the extracted text
    with open('output.txt', 'w') as output_file:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                output_file.write(text)
                output_file.write("\n\n")  # Add some spacing between pages