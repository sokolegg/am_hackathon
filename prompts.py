QUESTION_PROMPT = """
Only Based on next information write 10 questions for medical students
For right answers use exactly answers from the INFORMATION
For wrong answers imagine some wrong unmentioned stuff (but far away from original)
Each question must contain 5 options and <k> right answers for each question

Structure for your response
{"questions": [{"question": "... ? A) ... B) ...." , "right_answers": "*,*,"}, ...]}

RESULT JSON MUST CONTAINS 10 QUESTIONS WITH ONLY 2 fields: "question": str and right_answers: str 
Do not add any other fields!


INFORMATION:

"""


import random


def generate_question_prompt():
    k = random.randint(1, 5)
    right_answers = random.sample(["A", "B", "C", "D", "E"], k)
    return QUESTION_PROMPT.replace("<k>", str(k)).replace("<right>", ",".join(right_answers))


STORY_PROMPT = """
Only Based on next information write 10 story of different patients with provided disease or symptoms for medical exam.
Patient description is age, gender and some short story before hospital or doctor visit.

For right answers use exactly answers from the INFORMATION
For wrong answers imagine some wrong unmentioned stuff (but far away from original)
Each question must contain 5 options and <k> right answers for each question

Structure for your response
{"questions": [{"question": "The patient <patient_description> has ... ? A) ... B) ...." , "right_answers": "*,*,"}, ...]}

RESULT JSON MUST CONTAINS 10 QUESTIONS WITH ONLY 2 fields: "question": str and right_answers: str 
Do not add any other fields!


INFORMATION:

"""


def generate_story_prompt():
    k = random.randint(1, 5)
    right_answers = random.sample(["A", "B", "C", "D", "E"], k)
    return STORY_PROMPT.replace("<k>", str(k)).replace("<right>", ",".join(right_answers))