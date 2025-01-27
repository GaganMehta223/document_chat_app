import io
import os

import pytesseract
from flask import Flask, jsonify, request
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from PIL import Image

from utils import get_pdf_text, get_text_chunks, get_vectorstore

app = Flask(__name__)

conversation_chain = None
chat_history = {"chat_all_history": "", "chat_history": []}


def get_conversation_chain(vectorstore):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest")
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=vectorstore.as_retriever(), memory=memory
    )
    return conversation_chain


@app.route("/process_documents", methods=["POST"])
def process_documents():
    global conversation_chain
    raw_text = ""

    # Process PDF files
    pdf_files = request.files.getlist("pdfs")
    if pdf_files:
        raw_text += get_pdf_text(pdf_files)

    # Process Image files
    image_files = request.files.getlist("images")

    print("image_files")
    print(image_files)
    for image_file in image_files:
        print("opening")
        image = Image.open(image_file.stream)
        print("processing")
        raw_text += pytesseract.image_to_string(image)
    print(raw_text)
    print("raw_text")
    # Split text into chunks and create vectorstore
    if raw_text.strip():
        text_chunks = get_text_chunks(raw_text)
        vectorstore = get_vectorstore(text_chunks)
        conversation_chain = get_conversation_chain(vectorstore)
        return jsonify({"message": "Documents processed successfully."})
    else:
        return jsonify({"error": "No valid text found in uploaded documents."}), 400


@app.route("/chat", methods=["POST"])
def chat():
    global chat_history, conversation_chain
    user_question = request.json.get("user_question")
    chat_history["chat_all_history"] += f"User: {user_question}\n\n"

    response = conversation_chain({"question": chat_history["chat_all_history"]})
    bot_answer = response["answer"]

    chat_history["chat_history"].append({"role": "user", "content": user_question})
    chat_history["chat_history"].append({"role": "bot", "content": bot_answer})
    chat_history["chat_all_history"] += f"Bot: {bot_answer}\n"

    return jsonify(
        {"bot_answer": bot_answer, "chat_history": chat_history["chat_history"]}
    )


if __name__ == "__main__":
    app.run(debug=True)
