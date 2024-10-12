from mistralai import Mistral
import os
import random

api_key = random.choice([os.environ["MISTRAL_API_KEY"], os.environ["MISTRAL_API_KEY2"], os.environ["MISTRAL_API_KEY3"]])
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
