from question import Question #from question.py file import class Question

#question_prompts variable holding prompts list 
question_prompts = [
    "(1) What is a correct syntax to output 'Hello World' in Python?\n(a) print('Hello World')\n(b) p('Hello World)\n(c) echo('Hello World)\n(d) echo'Hello World'\n\n",
    "(2) How do you insert COMMENTS in Python code?\n(a) //This is a comment\n(b) /*This is a comment*/\n(c) #This is a comment\n\n",
    "(3) Which one is NOT a legal variable name?\n(a) _myvar\n(b) my_var\n(c) Myvar\n(d) my-var\n\n",
    '(4) Which of these collections defines a SET?\n(a) {"name": "apple", "color": "green"}\n(b) {"apple", "banana", "cherry"}\n(c) ("apple", "banana", "cherry")\n\n',
    '(5) Which collection does not allow duplicate members?\n(a) TUPLE\n(b) SET\n(c) LIST\n\n'
    
]
#assigning answers to questions
questions = [
    Question(question_prompts[0], 'a\n'),
    Question(question_prompts[1], 'c\n'),
    Question(question_prompts[2], 'd\n'),
    Question(question_prompts[3], 'b\n'),
    Question(question_prompts[4], 'b\n'),


]

#defined a function run_test
def run_test(questions):
    score = 0 #initialize a score by 0
    for question in questions: #iterate through questions
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1 #if answer is correct increment score by 1
            
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
    

run_test(questions)
