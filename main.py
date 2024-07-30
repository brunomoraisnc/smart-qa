# from getpass import getpass
from src.env_variables import LLM_MODEL_CONFIG

from langchain_google_genai import GoogleGenerativeAI

import streamlit as st


def main():
    st.set_page_config(page_title="Smart QA", layout="wide")

    st.title("Smart QA")
    
    with st.expander(label="Gemini Token Setup", expanded=True):
        st.markdown("""#### Instructions
1. Obtain a Google API Key at [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
    - If you don't have a Google Account, create one.
2. Click on the 'Generate key' button
3. Copy the generated API key and immediately paste it securely into the designated field within the app. <span style="color:red">Do not share this key with anyone</span>.
5. Delete the API Key after Use:

**For security purposes, it's essential to delete the API key once you've finished using the app.**

Return to the "API Key" page. Find the API key you generated and click the "Delete" button.
""", unsafe_allow_html=True)

        GOOGLE_API_KEY = st.text_input(
            label="Google API Key",
            placeholder="Insert your Google API Key here",
            type="password"
        )

    if GOOGLE_API_KEY == '':
        return None
    
    llm_instance = GoogleGenerativeAI(
        model="models/gemini-1.5-flash",
        google_api_key=GOOGLE_API_KEY,
        streaming=True,
        model_kwargs=LLM_MODEL_CONFIG
    )
    

    with st.form(key="question_form", clear_on_submit=True):
        question = st.text_area(
            label="Question",
            placeholder="Insert your question here"
        )
        submit_btn = st.form_submit_button("Submit")

        if submit_btn:
            st.text(f"Question: {question}")

            question_stream = llm_instance.stream(question)
            st.write_stream(question_stream)


if __name__ == "__main__":
    main()
