import pandas as pd
from mistralai import Mistral
import time

# Your API key should be a non-empty string
api_key = "KDanMXDVj36FcvO8diIecnSEHGaL4zPm"  # Replace with your actual API key
questions_file = "questions.csv"  # Replace with your file path


df = pd.read_csv(questions_file)

def question_prompt(body, possible_answer_a, possible_answer_b, possible_answer_c, possible_answer_d, possible_answer_e):
    return (
        "Answer the following question with the letters of the correct answer. Each question can have multiple answers that are right. "
        "Your answer must contain the letter of the answers, separated by commas and without any space. An ideal output is like: 'A,B', for instance. "
        "You don't provide any reasoning nor intuition nor explanation of your answer. You merely output the answer as per the instructions you are given. "
        "You only output the letters that you are asked to provide, e.g. 'A,B,C' or 'C'. Your answer is always sorted alphabetically. You must not put letters "
        "in a different order. "
        f"{body}\n"
        f"A: {possible_answer_a}\n"
        f"B: {possible_answer_b}\n"
        f"C: {possible_answer_c}\n"
        f"D: {possible_answer_d}\n"
        f"E: {possible_answer_e}\n"
    )

answers = []
s = Mistral(api_key=api_key,)

for row_idx, row in df.iterrows():
    prompt = question_prompt(
        row["question"],
        row["answer_A"],
        row["answer_B"],
        row["answer_C"],
        row["answer_D"],
        row["answer_E"]
    )
    
    time.sleep(5)

    chat_response = s.chat.complete(model="mistral-large-2402", messages=[
        {
            "content": prompt,
            "role": "user",
        },
    ])
    
    
    print(chat_response.choices[0].message.content)
    answers.append(chat_response.choices[0].message.content)

# output format is a 2-columns dataframe with exactly 103 rows
output_df = pd.DataFrame(answers, columns=["Answer"])
output_df.index.name = "id"
output_df.to_csv("output.csv")