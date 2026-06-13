import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_AI_KEY")
)
# client = genai.Client(
#     api_key="AQ.Ab8RN6LpcpwAnxoSfE3dtGsId_JIiYrMY5ZpiING0-RsHuVW0g"
# )

st.title("Smart AI Buddy")

question = st.text_input("Ask a question")

if st.button("Ask") and question:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )
        st.write(response.text)
    except Exception as e:
        st.error(str(e))
