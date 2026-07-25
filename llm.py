from ollama import chat


def ask_llm(question, context, conversation_history):

    messages = [

        {
            "role": "system",
            "content": (
                "You are a helpful study assistant. "
                "Answer using the provided PDF context. "
                "If the answer is not in the context, say so politely."
            )
        }

    ]

    # Add previous conversation
    messages.extend(conversation_history)

    # Add current question with retrieved context
    messages.append(
        {
            "role": "user",
            "content": f"""
PDF Context:

{context}

Current Question:
{question}
"""
        }
    )

    response = chat(
        model="qwen2.5:1.5b",
        messages=messages
    )

    return response["message"]["content"]