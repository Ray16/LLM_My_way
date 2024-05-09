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

def generate_slide_deck(file_name):
    # Placeholder function for generating the slide deck
    # Replace this with your actual slide deck generation logic
    pass

if __name__ == "__main__":
    main()