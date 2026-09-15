from rag.retrieval import retrieve_chunks
from rag.llm import generate_answer


FALLBACK_MESSAGE = (
    "I could not find the answer in the provided "
    "lecture content."
)


def build_context(retrieved_chunks):

    context = ""

    for chunk in retrieved_chunks:

        context += f"""
Lecture: {chunk["lecture_title"]}

Video time: {chunk["start"]} - {chunk["end"]} seconds

Content: {chunk["text"]}

---
"""

    return context


def create_prompt(question, context):

    prompt = f"""
You are a helpful teaching assistant.

Answer the user's question using ONLY the provided
lecture context.

Rules:

1. Use only the information available in the lecture context.
2. Do not use outside knowledge.
3. The answer can be directly stated or clearly implied
   by the lecture context.
4. If the lecture context does not contain enough
   information to answer the question, say exactly:

"I could not find the answer in the provided lecture content."

5. When possible, mention the lecture title and
   video timestamp where the answer was found.
6. Keep the answer clear and concise.

LECTURE CONTEXT:

{context}

USER QUESTION:

{question}

ANSWER:
"""

    return prompt


def answer_question(question):

    # -----------------------------
    # Step 1: Retrieve chunks
    # -----------------------------
    
    retrieved_chunks = retrieve_chunks(question)

    # -----------------------------
    # Step 2: No relevant chunks
    # -----------------------------

    if not retrieved_chunks:

        return {
            "answer": FALLBACK_MESSAGE,
            "sources": []
        }

    # -----------------------------
    # Step 3: Build context
    # -----------------------------

    context = build_context( retrieved_chunks)

    # -----------------------------
    # Step 4: Create prompt
    # -----------------------------

    prompt = create_prompt(
        question,
        context
    )

    # -----------------------------
    # Step 5: LLM
    # -----------------------------

    answer = generate_answer(prompt)

    # -----------------------------
    # Step 6: Return everything
    # -----------------------------

    return {
        "answer": answer,
        "sources": retrieved_chunks
    }