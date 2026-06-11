import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_AI_KEY")
)

st.title("ConceptBridge AI")

question = st.text_input("Ask a question")

if st.button("Ask"):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    st.write(response.text)