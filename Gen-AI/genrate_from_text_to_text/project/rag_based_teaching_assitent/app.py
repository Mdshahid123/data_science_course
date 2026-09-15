import streamlit as st

from rag.pipeline import answer_question


# --------------------------------
# Page configuration
# --------------------------------

st.set_page_config(
    page_title="RAG Teaching Assistant",
    page_icon="🎓",
    layout="wide"
)


# --------------------------------
# Custom CSS
# --------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 36px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #777;
        margin-bottom: 30px;
    }

    .source-card {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin-bottom: 12px;
    }

    .source-title {
        font-weight: 600;
        font-size: 17px;
    }

    .timestamp {
        font-size: 14px;
        color: #666;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------
# Header
# --------------------------------

st.markdown(
    '<div class="main-title">🎓 RAG Teaching Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Ask questions about your course lectures'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------
# Session state
# --------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


# --------------------------------
# Display previous messages
# --------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(
            message["content"]
        )

        if (
            message["role"] == "assistant"
            and "sources" in message
        ):

            sources = message["sources"]

            if sources:

                st.markdown("### 📚 Sources")

                for source in sources:

                    st.markdown(
                        f"""
                        <div class="source-card">

                        <div class="source-title">
                        {source["lecture_title"]}
                        </div>

                        <div class="timestamp">
                        ⏱ {source["start"]} -
                        {source["end"]} seconds
                        </div>

                        <p>
                        {source["text"]}
                        </p>

                        <small>
                        Similarity:
                        {source["similarity"]:.3f}
                        </small>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )


# --------------------------------
# Chat input
# --------------------------------

question = st.chat_input(
    "Ask something about the lecture..."
)


if question:

    # -----------------------------
    # Display user question
    # -----------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    # -----------------------------
    # Generate answer
    # -----------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "Searching lectures and generating answer..."
        ):

            result = answer_question(
                question
            )

        answer = result["answer"]

        sources = result["sources"]

        st.markdown(answer)

        # -------------------------
        # Sources
        # -------------------------

        if sources:

            st.markdown("### 📚 Sources")

            for source in sources:

                st.markdown(
                    f"""
                    <div class="source-card">

                    <div class="source-title">
                    {source["lecture_title"]}
                    </div>

                    <div class="timestamp">
                    ⏱ {source["start"]} -
                    {source["end"]} seconds
                    </div>

                    <p>
                    {source["text"]}
                    </p>

                    <small>
                    Similarity:
                    {source["similarity"]:.3f}
                    </small>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # -----------------------------
    # Save assistant message
    # -----------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": sources
        }
    )