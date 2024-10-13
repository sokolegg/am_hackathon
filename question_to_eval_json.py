import pandas as pd

# id,question,answer_A,answer_B,answer_C,answer_D,answer_E

def process():
    df_questions = pd.read_csv("benchmark/questions.csv")
    df_answers = pd.read_csv("benchmark/output.csv")

    # q = question A) answer_A B) answer_B C) answer_C D) answer_D E) answer_E
    q = []
    for i, row in df_questions.iterrows():
        q.append(f"{row['question']} A) {row['answer_A']} B) {row['answer_B']} C) {row['answer_C']} D) {row['answer_D']} E) {row['answer_E']}")

    # have to return {"messages": [{"role": "user", "content": "What should you do if a piece of tooth has broken off? A) Put it in milk or saliva B) Throw it away C) Put it in water D) Put it in alcohol E) Put it in juice"}, {"role": "assistant", "content": "A"}]}

    a = []
    for i, row in df_answers.iterrows():
        a.append(row["Answer"])

    with open("benchmark/eval_bench.jsonl", "w") as f:
        for i in range(len(q)):
            f.write(f'{{"messages": [{{"role": "user", "content": "{q[i]}" }}, {{"role": "assistant", "content": "{a[i]}" }}]}}\n')

if __name__ == "__main__":
    process()
