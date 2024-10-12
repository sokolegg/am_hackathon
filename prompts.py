QUESTION_PROMPT = """
Only Based on next information imagine 10 questions for medical students
For right answers use exactly answers from text
For wrong answers imagine some wrong umentioned stuff (but far away from original)
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
    return QUESTION_PROMPT.replace("<k>", str(k))



