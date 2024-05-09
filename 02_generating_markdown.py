import re

def create_markdown_file(text_res, filename):
    # Split the text_res into sections
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

**# {filename}**

Slides

---

**# 1. Background:**

{background}

---

**# 2. Challenge:**

{challenge}

---

**# 3. Current Status:**

{current_status}

---

**# 4. Method:**

{method}

---

**# 5. Result:**

{result}

---

**# 6. Conclusion:**

{conclusion}

---

**# 7. Outlook:**

{outlook}

---

**# Thank you!**
"""
    
    # Save the markdown content to a file
    with open(f'{filename}.md', 'w') as file:
        file.write(markdown_content)

# Example usage
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

filename = 'presentation'
create_markdown_file(text_res, filename)