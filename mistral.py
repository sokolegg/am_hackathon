from mistralai import Mistral
import os

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)


def invoke(prompt: str):
    response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ]
    )
    result = response.choices[0].message.content
    print(result)

    return result


if __name__ == "__main__":
    invoke("What is the capital of France?")  # Paris
