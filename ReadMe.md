# Chat with Documents and Images

This is a web application built with Streamlit and Flask, allowing users to upload documents and images, process them, and interact through a chatbot that answers questions based on the content of the uploaded files. It uses AI models and various libraries for document processing and image-to-text conversion.

## Features
- Upload PDFs and images (PNG, JPG, JPEG) for processing.
- Chat with the bot based on the content of your documents and images.
- Display chat history.
- Process documents and images using Tesseract OCR for images and custom text extraction for PDFs.

## Requirements

- Python 3.7 or later
- Streamlit
- Flask
- Requests
- Loguru
- Langchain
- pytesseract
- PIL (Pillow)
- FAISS
- Google Generative AI (for Chat)

Install required dependencies using:

```
pip install -r requirements.txt
```
# Steps to Run

## Backend Setup (Flask):

- Clone the repository and navigate to the backend directory.
- Install the required dependencies (listed in `requirements.txt`).
- Run the Flask server:

```
python app.py
```

- This will start the Flask backend server at http://127.0.0.1:5000.

# Frontend Setup (Streamlit):
- Clone the repository and navigate to the frontend directory.
- Install the required dependencies (listed in requirements.txt).
- Run the Streamlit app
```
streamlit run app.py

```

# Application Workflow

This will launch the frontend interface in your browser.

## Upload Files
Users can upload PDF documents and image files (PNG, JPG, JPEG) via the sidebar.

## Process Files
The user can click the "Process Files" button to send the uploaded files to the Flask backend for processing. The backend extracts text from PDFs and uses Tesseract OCR for images to get the text.

## Chat with the Bot
The user can ask a question related to the uploaded documents or general topics. The app sends the question to the Flask backend, where the chatbot generates a response based on the documents' content.

## Chat History
The chat history is displayed for easy reference.

# How It Works

## Backend (Flask)
The backend handles:
- Receiving and processing uploaded documents and images.
- Extracting text from PDFs and images using custom functions.
- Using the Langchain library to interact with Google Generative AI for answering user queries.
- Storing chat history and providing responses to user questions.

## Frontend (Streamlit)
The frontend:
- Allows users to upload files.
- Displays a user-friendly interface for interacting with the chatbot.
- Displays the chat history for context.

# Troubleshooting
- Ensure both the Flask backend and the Streamlit frontend are running simultaneously.
- If there are issues connecting to the backend, ensure the Flask server is running at the correct address (`http://127.0.0.1:5000`).
- If the text extraction from images or PDFs isn't working as expected, ensure the file quality is good.

### **Developed by Gagan Mehta ❤️☕**







