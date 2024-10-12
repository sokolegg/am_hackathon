import pandas as pd
from mistralai import Mistral
import time

# Your API key should be a non-empty string
api_key = "KDanMXDVj36FcvO8diIecnSEHGaL4zPm"  # Replace with your actual API key
questions_file = "questions.csv"  # Replace with your file path


df = pd.read_csv(questions_file)

def question_prompt(body, possible_answer_a, possible_answer_b, possible_answer_c, possible_answer_d, possible_answer_e):
    return (
        f"""Vous êtes un assistant IA médical expert, spécialement formé aux pratiques et procédures médicales françaises. Votre tâche est de répondre à des questions à choix multiples d'un examen de pratique médicale française. Veuillez suivre attentivement ces directives :

            Lisez la question en profondeur, en prêtant une attention particulière à tous les détails médicaux fournis.
            Examinez chaque option de réponse (A, B, C, D, E) individuellement et en combinaison avec les autres.
            N'oubliez pas que plusieurs options peuvent être correctes pour une seule question. Toutes les combinaisons possibles de A, B, C, D et E sont des réponses potentiellement valides.
            Appuyez-vous sur vos vastes connaissances des pratiques médicales françaises, des avancées récentes en science médicale et des directives cliniques standard pour éclairer vos décisions.
            Si certaines informations semblent ambiguës ou pourraient mener à plusieurs interprétations, considérez le scénario le plus probable dans un contexte médical français.
            Votre réponse doit UNIQUEMENT consister en les lettres correspondant aux options correctes, séparées par des virgules sans espaces. Par exemple : "A,B,E" ou "C" ou "A,B,C,D,E".
            Ne fournissez aucune explication, raisonnement ou contexte supplémentaire. Donnez uniquement la réponse dans le format spécifié ci-dessus.
            Assurez-vous que votre réponse est basée sur des connaissances médicales factuelles plutôt que sur des suppositions ou des hypothèses.
            Si vous n'êtes pas sûr d'une réponse, utilisez votre meilleur jugement basé sur les informations médicales dont vous disposez. Il vaut mieux inclure une option potentiellement correcte que de l'omettre si vous êtes incertain.
            Votre réponse doit toujours être dans l'ordre alphabétique. Par exemple, "A,C,E" est correct, mais "E,A,C" ne l'est pas.

            Voici la question :{body}\n
            
            A : {possible_answer_a}\n
            B : {possible_answer_b}\n"
            C : {possible_answer_c}\n"
            D : {possible_answer_d}\n"
            E : {possible_answer_e}\n"
            Fournissez votre réponse dans le format spécifié."""
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

    chat_response = s.chat.complete(model="mistral-large-latest", messages=[
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