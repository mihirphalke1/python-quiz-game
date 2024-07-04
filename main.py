from data import question_data
from question_model import QuestionModel
from quiz_brain import QuizBrain
import html

question_bank=[]

for ques in question_data:
    text=html.unescape(ques["question"])
    answer=ques["correct_answer"]
    question=QuestionModel(text, answer)
    question_bank.append(question)
    
quiz= QuizBrain(question_bank)

while QuizBrain.still_has_questions(quiz):
    quiz.next_question()
    if quiz.question_number==10:
        break

print("Hurray! You've completed the quiz")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")