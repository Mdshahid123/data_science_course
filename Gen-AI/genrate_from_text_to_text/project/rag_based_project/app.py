
import streamlit as st

from rag.stream_response import generate_response
from rag.augmentaion import create_prompt


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="AI Lecture Assistant",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------
# Header
# -----------------------------

st.title("🤖 AI Lecture Assistant")

st.write(
    "Ask questions about your course lectures."
)


# -----------------------------
# Chat history
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------
# User input
# -----------------------------

user_question = st.chat_input(
    "Ask something about the lecture..."
)


if user_question:

    # Display user question
    with st.chat_message("user"):
        st.markdown(user_question)

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )


    # -----------------------------
    # Create RAG prompt
    # -----------------------------

    prompt = create_prompt(user_question)


    # -----------------------------
    # Generate streaming response
    # -----------------------------

    with st.chat_message("assistant"):

        response_placeholder = st.empty()

        full_response = ""

        for chunk in generate_response(prompt):

            full_response += chunk

            response_placeholder.markdown(
                full_response
            )


    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": full_response
        }
    )

