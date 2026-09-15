<!-- Project overview & setup guide -->



# 🤖 RAG-Based AI Lecture Assistant

An AI-powered Lecture Assistant built using **Retrieval-Augmented Generation (RAG)**.  
The system allows students to ask questions about lecture content and receive answers based only on the relevant lecture context.

The project uses **embeddings, similarity search, Ollama, Llama 3.2, and Streamlit** to build an interactive AI teaching assistant.

---

## 🚀 Features

- 🎓 Ask questions about lecture content
- 🔍 Semantic search using embeddings
- 📚 Retrieve relevant lecture chunks
- 🧠 Retrieval-Augmented Generation (RAG)
- 🤖 Local LLM using Ollama
- ⚡ Streaming LLM responses
- 💬 Interactive Streamlit chat interface
- ⏱️ Lecture timestamps in responses
- 🛡️ Reduces hallucination by restricting answers to lecture context
- 💾 Chat history using Streamlit session state

---

## 🏗️ Architecture

```text
                    Student
                       │
                       ▼
               ┌───────────────┐
               │  Streamlit UI │
               └───────┬───────┘
                       │
                       ▼
                User Question
                       │
                       ▼
               ┌───────────────┐
               │   Retrieval   │
               │    System     │
               └───────┬───────┘
                       │
                       ▼
             Top Matching Chunks
                       │
                       ▼
               ┌───────────────┐
               │  Augmentation │
               │ Create Prompt  │
               └───────┬───────┘
                       │
                       ▼
               ┌───────────────┐
               │    Ollama     │
               │   Llama 3.2   │
               └───────┬───────┘
                       │
                    Streaming
                       │
                       ▼
               ┌───────────────┐
               │ Streamlit UI  │
               │    Response   │
               └───────────────┘