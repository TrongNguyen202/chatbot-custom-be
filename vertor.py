from VectorStore import VectorStore
import numpy as np


def answer_pro(promt):
    # Establish a VectorStore instance
    # print("promt", promt)
    print("message get", promt)
    vector_store = VectorStore()  # Creating an instance of the VectorStore class

    # Load data from file in 10-line chunks
    sentences = []
    with open('data.txt', 'r', encoding='utf-8') as file:
        chunk = []  # Temporary list to store 10 lines
        for line in file:
            chunk.append(line.strip())  # Add the current line to the chunk
            if len(chunk) == 10:  # Once we have 10 lines
                sentences.append(" ".join(chunk))  # Join them into a single string and add to sentences
                chunk = []  # Reset the chunk for the next 10 lines
        if chunk:  # Add any remaining lines as the last sentence if not exactly 10
            sentences.append(" ".join(chunk))

    # Tokenization and Vocabulary Creation
    vocabulary = set()
    for sentence in sentences:
        tokens = sentence.lower().split()
        vocabulary.update(tokens)
    word_to_index = {word: i for i, word in enumerate(vocabulary)}

    # Sentence Vectors
    sentence_vectors = {}
    for sentence in sentences:
        tokens = sentence.lower().split()
        vector = np.zeros(len(vocabulary))
        for token in tokens:
            vector[word_to_index[token]] += 1
        sentence_vectors[sentence] = vector

    for sentence, vector in sentence_vectors.items():
        vector_store.add_vector(sentence, vector)

    # Query vector creation
    query_sentence = promt
    query_vector = np.zeros(len(vocabulary))
    query_tokens = query_sentence.lower().split()
    for token in query_tokens:
        if token in word_to_index:
            query_vector[word_to_index[token]] += 1

    similar_sentences = vector_store.find_similar_vectors(query_vector, num_results=4)
    result = [sentence for sentence, similarity in similar_sentences]
    # print(result)
    # Re-load data.txt as individual lines for context extraction
    with open('data.txt', 'r', encoding='utf-8') as file:
        all_lines = [line.strip() for line in file.readlines()]
    # print(all_lines)
    # Extract 10-line chunks for context
    context_snippets = []
    for chunk_sentence in result:
        for i in range(0, len(all_lines), 10):  # Iterate through 10-line chunks
            chunk = " ".join(all_lines[i:i + 10])  # Create the chunk string
            if chunk_sentence == chunk:  # Check if chunk matches the result sentence
                # Get lines before and after chunk (if possible)
                before = all_lines[i - 10:i]  # Lines before the chunk
                after = all_lines[i + 10:i + 20]  # Lines after the chunk

                # Combine before, chunk_sentence, and after into one string
                context_snippets.append(" ".join(before) + " " + chunk_sentence + " " + " ".join(after))
                context_snippets.append("")  # Blank line for separation
                break # Exit the loop once a match is found

    # Write context snippets to a new file
    # with open('contextual_results.txt', 'w', encoding='utf-8') as file:
    #     for line in context_snippets:
    #         file.write(line + '\n')
    # print("context_snippets",context_snippets)
    return context_snippets


# Example call
# answer_pro("bạn có thể tìm cho tôi cái nào size L có thiết kế in lụa màu đen và form oversized không?")

# answer_pro("bạn có áo Unisex Teelab không?")
