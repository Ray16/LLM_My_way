from openai import OpenAI
from dotenv import load_dotenv
import PyPDF2
import os
from glob import glob

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("API_KEY")

# Instantiate API client
client = OpenAI(api_key=api_key)

os.makedirs('output', exist_ok=True)

def summarize_pdf(pdf_path):
    # Open PDF file
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Initialize an empty string to store the extracted text
        text = ""
        
        # Iterate over PDF pages
        for page in pdf_reader.pages:
            # Add text to string
            text += page.extract_text()
    
    # Create a chat completion task to summarize the extracted text
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"{text}"},
            {"role": "user", "content": "Read the paper, and summarize in 50 words each about the following:\n\n1. Background\n2. Challenge\n3. Current status\n4. Method\n5. Result\n6. Conclusion\n7. Outlook\n"}
        ]
    )
    
    # Open a file in write mode
    pdf_filename = os.path.basename(pdf_path)
    
    # Open a file in write mode using the extracted filename
    with open(os.path.join("output", f"{pdf_filename}_output.txt"), "w") as file:
        file.write(completion.choices[0].message.content)
    
    print(f"Written to {pdf_path}_output.txt")