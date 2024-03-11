''' Ask the user how many student are taking the test '''

user_number = int(input('How many student are taking the test? ')) 

'''Register each student'''
student_list = [ input(f'Student {x + 1}: ') for x in range(user_number)]

score_list = []
''' Call Each student one after the other to take the test '''
for each_student in student_list:
    print(f'\n{each_student}, Its time for your test.\n')

    '''The Test'''

    questions = ['1. What is my name\na.) Arise Damilare b.) Arise Damilola',
                 '2. Am I a Male\na.) Yes b.) No',
                 '3. Do you love your president\na.) Yes b.) No'
                 ]
    answers = ['a', 'a', 'a']
    score = 0
    for question, answer in zip(questions, answers):
        print(question)
        user_ans = input('Answer: ').strip().lower()

        if user_ans == answer:
            print('correct')
            score +=5

    print(f'Thanks for taking the test your total is {score}')
    score_list.append(score)


print(student_list)
print(score_list)