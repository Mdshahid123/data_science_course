
from rag.retrieval import top_matching_chunks
def create_prompt(input_query):

    # Creating LLM context
    context = ""

    for top_matching_chunk in top_matching_chunks:

        context += f"""
Lecture: {top_matching_chunk["lecture_title"]}

Video time: {top_matching_chunk["start"]} - {top_matching_chunk["end"]} seconds

Start time: {top_matching_chunk["start"]}

End time: {top_matching_chunk["end"]}

Content: {top_matching_chunk["text"]}

---
"""

    # Creating prompt for LLM
    prompt = f"""
You are a helpful teaching assistant.

Answer the user's question using only the provided lecture context.

Rules:

1. Use the lecture context to answer the question.

2. Do not make up information.

3. If the answer is not available in the lecture context, say:

"I could not find the answer in the provided lecture content."

4. When possible, mention the lecture title and video timestamp where the answer was found.

LECTURE CONTEXT:

{context}

USER QUESTION:

{input_query}

ANSWER:
"""

    return prompt