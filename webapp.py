import streamlit as st
import os

def main():
    st.set_page_config(page_title="LLM MY Way through research")
    st.title("LLM MY Way through research")

    uploaded_file = st.file_uploader("Upload research paper", type=["pdf"])

    if uploaded_file is not None:
        # Save the uploaded file
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getvalue())

        if st.button("Generate slide deck"):
            # Placeholder function for generating the slide deck
            generate_slide_deck(uploaded_file.name)

            # Rename the file for download
            renamed_file = f"slide_deck_{uploaded_file.name}"
            os.rename(uploaded_file.name, renamed_file)

            # Display a download link for the renamed file
            with open(renamed_file, "rb") as f:
                st.download_button("Download slide deck", f, file_name=renamed_file)

def generate_slide_deck(pdf_path):
    # Part 1: get GPT response
    from openai import OpenAI
    from dotenv import load_dotenv
    import PyPDF2
    import os
    from glob import glob

    # Load environment variables from .env file
    # load_dotenv()

    # # Get API key from environment variable
    # api_key = os.getenv("API_KEY")

    # # Instantiate API client
    # client = OpenAI(api_key=api_key)

    # os.makedirs('output',exist_ok=True)
    
    # with open(pdf_path, 'rb') as file:
    #     pdf_reader = PyPDF2.PdfReader(file)
    #     text = ""

    #     # Iterate over PDF pages
    #     for page in pdf_reader.pages:
    #         # Add text to string
    #         text += page.extract_text()

    # # Create a chat completion task to summarize the extracted text
    # completion = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "system", "content":
    #          f"{text}"},
    #         {"role": "user", "content": "Read the paper, and summarize in 50 words each about the following:\n\n1. Background\n2. Challenge\n3. Current status\n4. Method\n5. Result\n6. Conclusion\n7. Outlook\n"}
    #     ]
    # )

    # text_res = completion.choices[0].message.content

    # example text_res, comment out the above for gpt response
    text_res = """
    Background:
    This is the background section.

    Challenge:
    This is the challenge section.

    Current Status:
    This is the current status section.

    Method:
    This is the method section.

    Result:
    This is the result section.

    Conclusion:
    This is the conclusion section.

    Outlook:
    This is the outlook section.
    """

    # Part 2: generate markdown
    import re
    sections = re.split(r'\n\n', text_res)
    
    # Extract the relevant sections
    background = ''
    challenge = ''
    current_status = ''
    method = ''
    result = ''
    conclusion = ''
    outlook = ''
    
    for section in sections:
        if section.startswith('Background:'):
            background = section.replace('Background:', '').strip()
        elif section.startswith('Challenge:'):
            challenge = section.replace('Challenge:', '').strip()
        elif section.startswith('Current Status:'):
            current_status = section.replace('Current Status:', '').strip()
        elif section.startswith('Method:'):
            method = section.replace('Method:', '').strip()
        elif section.startswith('Result:'):
            result = section.replace('Result:', '').strip()
        elif section.startswith('Conclusion:'):
            conclusion = section.replace('Conclusion:', '').strip()
        elif section.startswith('Outlook:'):
            outlook = section.replace('Outlook:', '').strip()
    
    # Create the markdown content
    markdown_content = f"""---
marp: true
---

# {pdf_path}

Slides

---

# 1. Background:

{background}

---

# 2. Challenge:

{challenge}

---

# 3. Current Status:

{current_status}

---

# 4. Method:

{method}

---

# 5. Result:

{result}

---

# 6. Conclusion:

{conclusion}

---

# 7. Outlook:

{outlook}

---

# Thank you!
"""
        
        # Save the markdown content to a file
    output_name = f'{pdf_path}.md'
    with open(output_name, 'w') as file:
        file.write(markdown_content)

    print("=== Done generating markdown")
    return output_name


if __name__ == "__main__":
    main()