from data import question_data
from question_model import Question

question_bank = []
for data in question_data:
    question_bank.append(Question(data['text'], data['answer']))

