from prompts import generate_question_prompt, generate_story_prompt
import os
from mistral import invoke
import json
import random
from multiprocessing import Pool

jsons_dir = "data/jsons/"


def process_txts_folder(folder: str):
    for filename in random.sample(os.listdir(folder), len(os.listdir(folder))):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()

                generate_f = random.choice([generate_question_prompt, generate_story_prompt])
                prompt = generate_f() + text
                questions = invoke(prompt)
                # delete '''json and ''' if exists
                questions = questions.replace("```json", "").replace("```", "")
                random_id = random.randint(0, 100000)
                new_filename = filename.replace(".txt", f"_{random_id}.json")
                new_file_path = os.path.join(jsons_dir, new_filename)
                with open(new_file_path, 'w', encoding='utf-8') as file:
                    file.write(questions)
                print(f"Processed: {filename} -> {new_filename}")


if __name__ == "__main__":
    pool = Pool(16)
    pool.map(process_txts_folder, ["data/nhs_pages_txt/", "data/mayo_txt"] * 16)


