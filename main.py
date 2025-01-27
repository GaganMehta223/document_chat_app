import os

import requests
import streamlit as st
from dotenv import load_dotenv
from loguru import logger

from htmlTemplates import bot_template, css, user_template

load_dotenv()
# Flask backend URL
API_BASE_URL = os.getenv("API_BASE_URL")

# Page configuration
st.set_page_config(
    page_title="Chat with Documents and Images", page_icon=":books:", layout="wide"
)
st.write(css, unsafe_allow_html=True)

# Add a custom banner with an image icon
st.markdown(
    """
    <div style="background-color:#6C63FF;padding:10px;border-radius:10px;text-align:center;color:white;">
        <h1>Chat with Your Documents and Images 📚</h1>
        <p>Upload, process, and interact with your documents and images seamlessly!</p>
    </div>
    """,
    unsafe_allow_html=True,
)


# Reset session state when a new session starts
if "session_initialized" not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.chat_all_history = ""
    st.session_state.session_initialized = True  # Marks the session as initialized

# Sidebar for Document and Image Processing
with st.sidebar:
    st.title(":page_with_curl: Upload and Process")
    pdf_docs = st.file_uploader(
        "Upload your PDFs here:", accept_multiple_files=True, type=["pdf"]
    )
    image_files = st.file_uploader(
        "Upload your Images here:",
        accept_multiple_files=True,
        type=["png", "jpg", "jpeg"],
    )

    if st.button("Process Files"):
        try:
            if pdf_docs or image_files:
                with st.spinner("Processing your files..."):

                    files = [("pdfs", pdf) for pdf in pdf_docs] + [
                        ("images", img) for img in image_files
                    ]
                    response = requests.post(
                        f"{API_BASE_URL}/process_documents", files=files
                    )

                    if response.status_code == 200:
                        st.success("Documents and images processed successfully.")
                    else:
                        st.error(
                            f"Failed to process documents and images: {response.text}"
                        )
                        logger.error(
                            f"Error processing documents/images: {response.text}"
                        )
            else:
                st.warning("Please upload at least one PDF or image.")
        except requests.exceptions.RequestException as e:
            st.error("Unable to connect to the backend. Please try again later.")
            logger.error(f"Backend connection error: {e}")

# Main section for Chat Functionality
st.subheader(":speech_balloon: Chat Section")

# Two-column layout for chat and additional info
col1, col2 = st.columns([3, 1])

with col1:
    user_question = st.text_input(
        "Ask a question about your documents or general topics:"
    )
    if user_question:
        try:
            with st.spinner("Fetching response..."):
                response = requests.post(
                    f"{API_BASE_URL}/chat", json={"user_question": user_question}
                )
                if response.status_code == 200:
                    data = response.json()
                    bot_answer = data.get("bot_answer", "No response received.")
                    chat_history = data.get("chat_history", [])

                    # Update session state
                    st.session_state.chat_all_history += (
                        f"User: {user_question}\nBot: {bot_answer}\n"
                    )
                    st.session_state.chat_history = chat_history

                    # Display chat history
                    for message in chat_history:
                        if message["role"] == "user":
                            st.markdown(
                                user_template.replace("{{MSG}}", message["content"]),
                                unsafe_allow_html=True,
                            )
                        else:
                            st.markdown(
                                bot_template.replace("{{MSG}}", message["content"]),
                                unsafe_allow_html=True,
                            )
                else:
                    st.error(
                        f"Failed to get a response from the chatbot: {response.text}"
                    )
                    logger.error(f"Error in chatbot response: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error("Unable to connect to the backend. Please try again later.")
            logger.error(f"Backend connection error: {e}")

with col2:
    st.info("Pro Tips:")
    st.markdown(
        """
        - Upload high-quality PDFs and images for better results.
        - Ask specific questions for precise answers.
        - Use this app for quick analysis of your documents and images.
        """
    )

# Footer section
st.markdown(
    """
    <hr>
    <div style="text-align:center;">
        <p>Developed with ❤️ and ☕ by Gagan Mehta</p>
    </div>
    """,
    unsafe_allow_html=True,
)
