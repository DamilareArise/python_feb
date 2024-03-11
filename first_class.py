# print('My name is Damilare')

# print(''' 
#     wuehwewehweqweiqwheqwe
#     hdqwdgqwjkdhqwhdqw
#     dghqkwdqgwkjdqhwhqwd
#     wkjdhajdhaldkada

# ''')

# print('My name ' + '67')

# Python Variables
'''
1. Variable Name

Rules guiding variable name declaration
i. It must be descriptive
ii. It must not start with any character except '_' and any alphabet
iii. A variable name declaration does not allow space inbetween the words
    you can use the following method to join them together
    a. snake casing
        my_first_name
    b. Pascal casing
        MyFirstName
    c. Camel casing 
        myFirstName



2. Assignment operator
3. Item/content

'''

bottle = 'Water'
# print(bottle)

bottle = 'Wine'
# print(bottle)

# first_name_of_student = 'Dami'
# FirstNameOfStudent = ""
# firstNameOfStudent = ''


first_name = 'Damilare'
last_name = 'Arise'
age = 10
height = 5.7

# print('My name is', first_name)

# using the + method
# print('You are welcome ' + str(height))

# using comma method
# print('You are welcome', height)

# using f-string method
# print(f'Welcome to class {first_name} {last_name}, you are {age}years old.')

# using str.format method 
# print('My name is {} {}'.format(first_name, last_name))



'''
        PYTHON DATATYPE
1. Text type; strings, str() e.g 'Banana', '55'

2. Number type;
    i.  integers, int() e.g 45, 6
    ii. float, float() e.g 45.4, 2.004
    iii. complex, complex() e.g 1 + 1j, 3 + 5j

3. Boolean type; bool(),  True == 1, False == 0

4. sequence type;
    i. list, list() e.g [25, 35, 56, 60], ['Banana', 'Adebayo', True, 45, 3 + 5j]
    ii. tuple, tuple() e.g (25, 35, 56, 60), ('Banana', 'Adebayo', True, 45, 3 + 5j)
    iii. range, range() e.g range(20)

5. mapping type;
    python dictionary; dict() e.g {'name':'Jesulayomi', 'matric_no':'DSE101'}

6. Set type; set() e.g {3, 5, 2, 6, 1, 4}, {'Bisola', 'Jesulayomi', 'Abimbola'}

7. Binary type; byte, bytearray, memoryview

'''

car = 'Lexus' #['L', 'e', 'x', 'u', 's']
# print(car[0])

value = str(67)

# print(type(value))
val = (9.6+0j)

val = False

# print(type(val))

list_python_student = ['Tuminu', 'Joshua', 'Habeeb', 23, 565.5, True, ['yam', 'rice']]
# print(type(list_python_student))
# print(list_python_student[-1][-1])

my_tuple = ('Tuminu', 'Joshua', 'Habeeb', 23, 565.5, True, ['yam', 'rice'], ('password', 'username'))

# print(my_tuple[-1][0][2])

my_range = range(1, 21)
# print(my_range)

# print(list(my_range))


# student_details = {'Name':'Toluwanimi', 'Gender':'Female', 'Dept':'AI'}
# print(type(student_details))


my_set = {5, 7, 8, 6, 4, 1, 2, 9, 3}
my_set2 = {'David', 'Marv', 'Maimunat', 'Toluwanimi'}
# print(my_set2)


num = 'Damilare'
# print(bin(num))

# print(bytearray(num, 'utf8'))
# bytes
# memoryview

'''
    PYTHON OPERATORS
1. Arithmetic operator e.g +, -, *, **, /, //, %
2. Assignment operator e.g =, +=, -=, /=, //=, **=, *=, %=
3. Identity operator  e.g is, is not
4. comparison operator e.g ==, !=, >, <, >=, <=
5. Logical operator e.g and, or, not
6. Membership operator e.g in, not in
7. Bitwise operator e.g & , | , ~, ^, <<, >>
    # & 	AND	Sets each bit to 1 if both bits are 1
    # |	    OR	Sets each bit to 1 if one of two bits is 1
    # ^	    XOR	Sets each bit to 1 if only one of two bits is 1
    # ~ 	NOT	Inverts all the bits
    # <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
    # >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

'''

# print(7%2)

# cup = 'water'
# print(cup)

# val = 5
# val *= 1 # val = val + 1
# print(val)

val = 5
# print(val == 6)
# print(val != 6)
# print(val >= 6)

obj1 = 'table'
obj2 = 'Table'
# print(obj1 is not obj2)

food1 = 'rice'
food2 = 'beans'
# print(food1 == 'Rice' or food2 == 'Beans')
# print(not food1)


student = ['habeeb', 'tumininu', 'toluwanimi', 'maimunat']
# print('Habeeb' not in  student)

val1 = bin(20)
val2 = bin(40)
# print(bin(20 & 40))
a = 7
b = 3

# concatenation
# print(f'{a} + {b} = {a + b}')
# print(a, '+', b, '=', a+b)
# print(str(a) + ' + ' + str(b)+ ' = ' + str(a+b) )

# print(f'{val1} ^ {val2} = {bin(20 ^ 40)}')
# print(bin(~40))

# print(bin(40 >> 2))


# Python condition statement(if, else, elif)

# x = 5
# y = 2

# if x == 5 and y == 1 :
#     print(f'{x} is equal to 5 ')
# else:
#     print(f'{x} is not equal to 5 ')


# ussd = input('USSD Code: ')

# if ussd == '*312#':
#     print('''
#     1. Data plan
#     2. Check balance  
#     ''')

#     user = input('Choice: ')
#     if user == '1':
#         print('''
#               DATA PLAN
#         1. Daily Plan
#         2. Weekly Plan
#         3. Monthly Plan 
#         ''')
        
   
#     elif user == '2':
#         print("CHECK BALANCE")
#     else:
#         print('Invalid command')

# else:
#     print('Invalid ussd code! ')


# user = input('autorenew?, yes or no? ')
# if user == 'yes':
#     print('Autorenew successful')
# elif user == 'Yes':
#     print('Autorenew successful')
# elif user == 'YES':
#     print('Autorenew successful')
# else:
#     print('autorenew declined ')


# A simple Calculator v.1

# print('''
#         My ALATA Calculator

#     1. Addition
#     2. Subtraction
#     3. Division
#     4. Multiplication
#     *. Exit
      
#     ''')

# first_value = float(input('First Value: '))
# second_value = float(input('Second Value: '))

# user = input('Option: ')
# if user == '1':
#     result = first_value + second_value
#     print(f'Answer: {result}')

# elif user == '2':
#     result = first_value - second_value
#     print(f'Answer: {result}')

# elif user == '3':
#     result = first_value / second_value
#     print(f'Answer: {result}')

# elif user == '4':
#     result = first_value * second_value
#     print(f'Answer: {result}')

# elif user == '*':
#     exit()

# else:
#     print('Invalid command')


# PYTHON STRINGS

name = 'MARY has a little lamb. She loves food' #['M', 'A', 'R', 'Y']
# print(len(name))
# print(name[0])
# print(type(name))

# SOME FUNCTIONs A STR CLASS CAN PERFORM

# print(name.capitalize())
# print(name.lower())
# print(name.upper())
# print(name.title())


# user = input('autorenew?, yes or no? ') 
# if user.capitalize() == 'Yes':
#     print('Autorenew successful')
# else:
#     print('autorenew declined ')

# print(name.strip('^$'))


# user = input('autorenew?, yes or no? ').strip().capitalize() 
# if user == 'Yes':
#     print('Autorenew successful')
# elif user == 'No':
#     print('Stop autorenew')
# else:
#     print('autorenew declined ')

name = 'MARY has a little lamb. She loves food'
# print(name.split())
# print(name.split('.'))

word_split = name.split()
# print(word_split)

# word_join = '+'.join(word_split)
# print(word_join)

num = '23'
# print(num.isalpha())

# print(name.startswith('m'))
# print(name.endswith('food'))
# print(name.find('MARY'))


# print(name.center())
# name = input('Your name: ')
# user = input("Press enter to start the test or 1 to exit ")
# score = 0

# if user == '1':
#     exit()
# else:
#     print('1. Who is the president of nigeria?\na.) Buhari b.) BAT')
#     user = input('Answer: ').strip().capitalize()
#     if user == 'B':
#         print('correct')
#         score += 5
#     else:
#         print('Olodo ni e jor')

#     print('2. Capital of france\na.) Paris b.) London')
#     user = input('Answer: ').strip().capitalize()
#     if user == 'A':
#         print('correct')
#         score += 5

# print(f'Thanks for taking the test {name}, your total score is {score}')



#Python Escape Characters

expression = 'this is the path to my python file - C:\python_feb\\new_file\\read_python\\think_python'

# print(expression)

# \t  tab
# print('I am a\t\t\t genius')

# \b backspace
# print('I am a\b\b\b genius')

# \n  enter
# print('I am a\n\n genius')

# \r return
# print('I am a\r genius')

# r --> raw string

expression = r'this is the path to my python file - C:\python_feb\new_file\read_python\think_python'

# print(expression)


# PYTHON COLLECTIONS

'''
1. LIST [] or list() 
Properties of a class list
    i. Ordered
    ii. Changeable/mutable
    iii. It allows duplicate values 
    iv. It can be indexed

'''

my_list = ['Maimunat', 'Joshua', 'Bottle', 45, True, ['Yam', 'Rice', 'Semo'], 'Bottle']
# print(len(my_list))
# print(my_list[0])
# print(my_list[-4])
# print(my_list[-2][-2])
# print(my_list[5][1])

#slicing
# print(my_list[2:])
# print(my_list[4:6])

# my_list[0] = 'Mary'
# print(my_list)

# my_list[0:3] = ['Tolu', 'Marv',]
# print(my_list)

# Some Functions a list class can perform

li = []

# li.append(['Habeeb', 'Dave'])
# li.extend(['Habeeb', 'Dave'])

# my_list.clear()
# del my_list
# my_list.pop(4)
# my_list.remove('Bottle')
# my_list.remove('Bottle')
# my_list.reverse()
# my_list.insert(0, 'Habeeb')

# print(my_list.count('Bottle'))
# print(my_list.index('Maimunat'))


# print(li)
# print(my_list)

# num = [ 34, 56, 76 , 4]
# print(sum(num))
# print(max(num))
# print(min(num))

python_students = ['Tolu', 'Joshua', 'Mary', 'Maimunat', 'Marv']
# print('Melcome to class', python_students[0])
# print('Melcome to class', python_students[1])

# for each in python_students:
#     print('Melcome to class',each)
#     print('----------------------------')

# num = []
# for x in range(10):
#     num.append(x)

# print(num)

# name_of_student = [] 
# for x in range(10):
#     name = input(f'Name {x+1}: ')
#     name_of_student.append(name)

# print(name_of_student)

# questions = [
#     '1. Who is the president of nigeria?\na.) Buhari b.) BAT', 
#     '2. Capital of france\na.) Paris b.) London'
#     ]

# for each_quest in questions:
#     print(each_quest)
#     user = input('ans: ')


# Tuple (), tuple()

'''
1. unchangeable/immutable
2. they can be indexed
3. allows duplicate values
4. Ordered

'''

students = ('Damilare', 'slessor', 'slessor','maimunat', 'richard', 23, False, [23, 34 , 535])
# print(students)
# print(students[3])
# print(students[-3])
# print(students[1: 4])

# students[1] = 'Mary'
# list_students = list(students)
# # print(list_students)
# list_students[1] = 'Mary'
# # print(list_students)

# students = tuple(list_students)

# print(students)

# Unpacking
# (*list_students,) = students
# print(list_students)

# (*student1, student2, alls )= students
# print(student1)


# fruits = ('banana', 'mango', 'apple')
# (fruit1, fruit2, fruit3) = fruits
# # print(alls)
# print(fruit1)
# print(fruit2)
# print(fruit3)


# print(students.count('slessor'))
# print(students.index('slessor'))

# student = ['mary', 'lola', ' ayo', 'femi']
# scores = [23, 45, 95, 65]
# # print(max(scores))
# # index_max = scores.index(max(scores))

# # print(student[index_max])

# mean_score = sum(scores)/len(scores)
# print(mean_score)

names = ('mary', 'lola', ' ayo', 'femi')
scores = (23, 45, 95, 65)

# for name in names:
#     print(name)
   
# for name, score in zip(names,scores):
#     print(f'{name} scored {score}.')

# details = [('mary', 23), ('lola', 45), ('ayo', 95), ('femi', 65)]

# # print(details)
# for name, score in details:
#     print(f'{name} scored {score}.')


# exam = [('1. Who is the president of Nigeria a.) Buhari b.) BAT', 'b'), 
#         ('2. How many state are in Nigeria a.) 34 b.) 36', 'b')
#      ]

# score = 0

# for question, ans in exam:
#     print(question)
#     user = input('Answer: ').strip().lower()
#     if user == ans:
#         print('correct')
#         score += 5
#     else:
#         print('wrong')

# print('Your total score is', score)


#SET {}, set()

'''
1. Unchangeable/immutable
2. it can not be indexed
3. it is not ordered
4. it doesnt allow duplicate value
'''

myset = {'apple', 'pineapple', 'orange', 'cherry'}
# print(type(myset))
# myset[1] = 'watermelon'

setnum ={5, 4, 6, 7, 8, 9, 1, 3, 2}
# print(setnum)

# FUNCTIONS
# fruits = myset.copy()
# myset.add('watermelon')
# myset.update(['yam', 'beans'])
# myset.pop()

# print(myset)
# print(fruits)

# print(myset)
# balance = 500
# stake = float(input('Stake: '))


# while balance > 0 and balance > stake:

#     guess = input('guess the choosen fruit: ').strip().lower()
#     choosen_fruit = myset.pop()
#     myset.add(choosen_fruit)
#     # print(choosen_fruit)
    

#     if guess == choosen_fruit:
#         balance += 2 * stake
#         print(f'You guessed right.\nYour current balance is {balance}')
#     else:
#         balance -= stake
#         print(f'wrong\nYour current balance is {balance}')

#     user = input('press 1 to replay or # to exit')
#     if user == '#':
#         break

# else:
#     print('Insufficient fund. go and deposit.')

# print(f'Your cashout amount in {balance}')

# myset.remove('Apple')
# myset.discard('Apple')
# print(myset)

setA = {5, 4, 6, 7, 8, 9, 1, 3, 2, 10, 11}
setB = {3, 2, 4, 5, 6, 13, 12}
setC = {3, 2, 4, 5, 6}

# print(setA.union(setB))
# print(setA.intersection(setB))
# setA.intersection_update(setB)
# print(setA.difference(setB))
# print(setA - setB)

# setA.difference_update(setB)
# set4 = setA.symmetric_difference(setB)
# setA.symmetric_difference_update(setB)
# print(setA)
# print(set4)


# Dictionary {key:value}, dict(key=value)
'''
1. it is changeable
2. it is ordered
3. Duplicate is not allowed
'''

car = {'Model':'Tesla', 'Year':2022}
# print(type(car))
# print(car)
# print('The model is',car['Model'])
# car['Model'] = 'Benz'
# print(car)

car = {
    'Model':'Tesla', 
    'Year':2022,
    'Color':['Black', 'Blue'],
    'Year1':2021,
    'Owner':{
        'Name': 'Dami',
        'Price': 234567
    }
    }

# print(car['Owner']['Name'])
# FUNCTIONs

# for kk in car.keys():
#     print(kk)

# print(car.values())

# for key, value in car.items():
#     print(key)

# car.update({'Transmission': 'Automatic', 'EngineType':'V6'})
# print(car['color'])
# print(car.get('color', 'Not found'))
# car.popitem()
# car.pop('Color')
# print(car)


# {
#     'Student1':{'name':'Ade', 'MatNo':'23456'},
#     'Student2':{'name':'Ade', 'MatNo':'23456'},
# }


# user = input('Kindly press 1 to start registration: ')
# if user == '1':
#     x = 1
#     student_db = {}
#     while True:
        
#         name = input('Name: ').strip().title()
#         matno = input('MatNo: ').strip().title()

#         students = {'name':name, 'matno':matno}
#         student_db.update({f'student{x}':students})

#         x +=1
#         user = input('Press 1 stop or enter key to continue: ')
#         if user == '1':
#             break

#     print(student_db)




def landing_page():
    global value1
    global value2

    name = input('Name: ')
    value1 = float(input('Value 1: '))
    value2 = float(input('Value 2: '))

    user = input(f'''
            My Alata Calculator. Welcome {name}
        
        1. Addition
        2. Subtraction
        #. Exit

    Choose your operation: ''').strip()
    
    if user == '1':
        addition()
    elif user == '2':
        subtraction()
    elif user == '#':
        exit()
    else:
        print('Invalid Input')
        landing_page() # Recursive function

  

def addition():
    print(f'Ans: {value1 + value2}')
    decide()


def subtraction():
    print(f'Ans: {value1 - value2}')
    decide()


def decide():
    user = input('press 1 to go to home or # to exit: ').strip()
    if user == '1':
        landing_page()
    else: 
        exit()   



# landing_page()  
        

# def add(val1: float, val2: float = 10):
#     '''
#     I add things up
#     '''
#     return val1 + val2
#     # 20

# def arithmetic():
#     res = 2 ** add(10)
#     return res

# def printf(name):
#     print(f'{name}, your result is {arithmetic()}')

# printf(input('Your name: '))
        


class Dust:
   def __init__(self):
       self.first_name1 = 'Arise'
       self.last_name1 = 'Damilare'

    #    self.naming()

   def naming(self):
       print(f'My name {self.first_name1} {self.last_name1}')



father = Dust()
# father.last_name1

# print(type(tumininu))

# surname = 'Ojo'

# def call_name():
#     global fname
#     fname = input('First name: ').strip()
#     print('My name is', fname, surname)


# def say():
#     print(surname, fname)

# call_name()

# def call_name(name:str):
#     print('My name is', name)

# x = input('First name: ')
# call_name(x)



# basket = list()

# class Calculator:
#     def __init__(self):
#        self.calc_name = 'Casio'

#     #    self.home()

#     def home(self):
#         print(f'Welcome to {self.calc_name}')
#         self.value1 = float(input('First value: '))
#         self.value2 = float(input('Second value: '))
#         user = input('''
#             Choose your operation;
            
#               1. Addition
#               2. Subtraction
#               #. Exit
#         Option: ''')

#         if user == '1':
#             self.addition()
#         elif user == '2':
#             self.subtraction()
#         elif user == '#':
#             exit()
#         else:
#             print('Invalid Option, Try again! ')
#             self.home()

#     def addition(self):
#         print(f'Ans: {self.value1 + self.value2}')
#         self.decide()

#     def subtraction(self):
#         print(f'Ans: {self.value1 - self.value2}') 
#         self.decide()

#     def decide(self):
#         user = input('Press 1 to home or # to exit')
#         if user == '1':
#             self.home()
#         else:
#             exit





# mycalc = Calculator()
# mycalc.home()




# INHERITANCE

class Parent:
    def __init__(self):
        self.surname = 'Ojo'
        self.firstname = 'Mary'
        self.hobby = 'Eating'

        # self.describe()

    def describe(self):
        print(f'My name is {self.firstname} {self.surname}, I love {self.hobby}')

parent = Parent()


class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        #or
        # super().__init__()
        self.firstname = 'Maimunah'
        self.hobby = 'Sleeping'
        self.bestfood = 'Fufu and Egusi'

        # self.describe()

    def cooking(self):
        print(f'{self.firstname} is cooking {self.bestfood}')



child = Child()



class Grandchild(Child):
    def __init__(self):
        Child.__init__(self)
        self.firstname = 'Richard'
        self.hobby = 'Talking'

        # self.describe()

grandchild = Grandchild()
