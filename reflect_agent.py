from openai import OpenAI

client = OpenAI()

question = "Explain what a black hole is."

# STEP 1 — Generate answer
initial_response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user", "content": question}
    ]
)

draft = initial_response.choices[0].message.content

print("FIRST ANSWER:\n")
print(draft)

# STEP 2 — Reflection
reflection_response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a critic AI. "
                "Review the answer and find mistakes, missing details, "
                "or unclear explanations."
            )
        },
        {
            "role": "user",
            "content": f"Question: {question}\n\nAnswer:\n{draft}"
        }
    ]
)

reflection = reflection_response.choices[0].message.content

print("\nREFLECTION:\n")
print(reflection)

# STEP 3 — Improve answer
final_response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": (
                "Improve the answer using the critique."
            )
        },
        {
            "role": "user",
            "content": (
                f"Original Question:\n{question}\n\n"
                f"Draft Answer:\n{draft}\n\n"
                f"Critique:\n{reflection}"
            )
        }
    ]
)

final_answer = final_response.choices[0].message.content

print("\nFINAL IMPROVED ANSWER:\n")
print(final_answer)



if __name__ == "__main__":
    print("Hello from reflect Agent!")