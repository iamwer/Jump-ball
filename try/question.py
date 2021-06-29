from question import Question



question_prompts = [
    "What color are apples?\n(a) Red/Green\n Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n Red\n(c) Blue\n\n",
]

questions = [
    Question(question_prompts[0], "a")
    Question(question_prompts[1], "c")
    Question(question_prompts[2], "b")

]

def run_test(questions):
    score = 0
    for queston in questions:
        answer = input(question.prompt)
        if answer == queston.answer:
            score +=1
    print("You got " + str(score)+ "/" + str(len(quwstions)) + "correct")

run_test(questions)