import os
import json
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from config import EMBEDDING_DIRECTORY, TOP_K, SIMILARITY_THRESHOLD
from rag.embedding import create_embedding


def load_all_chunks():

    chunks = []

    files = os.listdir(EMBEDDING_DIRECTORY)

    for file in files:

        if not file.endswith(".json"):
            continue

        file_path = os.path.join(
            EMBEDDING_DIRECTORY,
            file
        )

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        for chunk in data["segements"]:

            chunks.append(chunk)

    return chunks


def retrieve_chunks(query):

    # -----------------------------
    # Step 1: Query → embedding
    # -----------------------------

    query_vector = create_embedding(query)

    query_vector_2d = [query_vector]

    # -----------------------------
    # Step 2: Load all chunks
    # -----------------------------

    chunks = load_all_chunks()

    if not chunks:
        return []

    # -----------------------------
    # Step 3: Extract embeddings
    # -----------------------------

    chunk_embeddings = [
        chunk["embedding"]
        for chunk in chunks
    ]

    # -----------------------------
    # Step 4: Cosine similarity
    # -----------------------------

    similarities = cosine_similarity(
        query_vector_2d,
        chunk_embeddings
    ).flatten()

    # -----------------------------
    # Step 5: Sort descending
    # -----------------------------

    sorted_indices = np.argsort(
        similarities
    )[::-1]

    # -----------------------------
    # Step 6: Top-K retrieval
    # -----------------------------

    retrieved_chunks = []

    for index in sorted_indices[:TOP_K]:

        score = float(similarities[index])

        if score < SIMILARITY_THRESHOLD:
            continue

        chunk = chunks[index].copy()

        chunk["similarity"] = score

        retrieved_chunks.append(chunk)

    return retrieved_chunks