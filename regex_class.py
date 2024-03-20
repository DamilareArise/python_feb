# Regular expressions are powerful tools for pattern matching and manipulation of strings. Python provides the re module, which allows you to work with regular expressions

# One of the fundamental operations with regex is pattern matching. You define a pattern using a combination of characters and special symbols that represent a specific set of strings you want to match

# example
import re

def check_for_email(email):

    pattern = r'^\w+@\w+\.\w+$'
   
    matches = re.match(pattern, email)
    # print(matches)

    if matches:
        print("Valid email")
    else:
        print('invalid email')

# inp = input('Email: ')

# check_for_email(inp)

# r = rawstring
# \w = matches one or more word characters (letters, digits, or underscores). 
# ^ = to comfirm/assert the start of a string
# \. =  matches the literal "." symbol.
# $ = asserts the end of the string.
# + = The + sign is a metacharacter in regular expressions that specifies that the preceding element should occur one or more times
# * = the * sign allows the pattern to match elements that can occur zero or more times, making them optional
# {} = The {} sign is a quantifier metacharacter in regular expressions that allows you to specify the exact number of occurrences of the preceding element. It allows you to specify a specific range or an exact count for the number of repetitions

# E.g
# \d{3} matches exactly three consecutive digits.
# [a-z]{2,4} matches a sequence of lowercase letters that is between 2 and 4 characters long.
# a{5} matches exactly five consecutive occurrences of the letter 'a'

# \d, \w, and \s - a digit, word, or space character, respectively.
# \D, \W, and \S - anything except a digit, word, or space, respectively.
# [abc] -	any character between the brackets (such as a, b, ).
# [^abc] - any character that isn’t between the brackets.

# pattern =r'[a-z]{2,4}'
# text = input('text: ')
# matchee = re.match(pattern, text)
# if matchee:
#     print('Valid')
# else:
#     print('Invalid')

# regex  method/Funtions 

# 1. match()

# pattern = r'abc'
# string = 'abc def '
# matche = re.match(pattern, string)
# # print(matche)
# if matche:
#     print('There is a match')
# else:
#     print('No match found')

# 2. search()

# pattern = r'abc'
# string = 'qabc abc abc'
# match = re.search(pattern, string)
# print(match)
# if match:
#     # print(match.group())
#     print('Match found')
# else:
#     print('No match found')

# 3. findall()

# pattern = r'\d{3}'
# string = 'I have 323 apples and 234 oranges 567'
# matches = re.findall(pattern, string)
# print(matches)

# 4. sub()

# pattern = r'\d+'
# string = 'I have 323 apples and 234 oranges 567'
# replacement = 'some'
# modified_string = re.sub(pattern, replacement, string)
# print(modified_string)


# 5. group()

# The .group() method is used to retrieve the matched substring or subgroups from a match object obtained through the re.match() or re.search() functions in Python.

# pattern = r'(\w+)-(\d+)-(\d+)'
# string = 'apple-123-3435 fasghjakdlfgldj sdjflg;dfk'

# match = re.search(pattern, string)
# if match:
    # print('Valid')
#     print(match)
    # print(match.group())
    # print(match.group(1))
    # print(match.group(2))
    # print(match.group(3))




pattern =r'(\+234) (\d{3}) (\d{3}) (\d{4})'
string = 'This is my phone number +234 803 456 2345 sjdasfjksfkfs +234 703 454 2343'
# matche = re.search(pattern, string)
# if matche:
#     print(f'valid - {matche.group()}')
# else:
#     print('Invalid')

# matche = re.findall(pattern, string)
# print(matche)
# if matche:
#     print(f'valid - {matche.group()}')
# else:
#     print('Invalid')


file = open(r"C:\Datasets\president_height.csv", mode='rt')
values = file.read()
# print(values)
# pattern = r'\d{3}'
# height = re.findall(pattern, values)
# print(height)


# pattern = r'(\d+),(\w+) (\w+),(\d+)'
# details = re.findall(pattern, values)
# print(details)



# # pattern = '[^abc]'


# Assignment
# 1. You can use regex to extract the domain names from a list of email addresses
# 2. You can use regex to parse and extract data from CSV (Comma-Separated Values) files.
# import re

csv_data = 'John,Doe,25,New_York\nJane,Smith,30,Chicago\nMark,Johnson,35,Los Angeles'
matches = re.findall(r'(\w+),(\w+),(\d+),(\w+)', csv_data)
# print(matches)

data = [{'first name':match[0], 'last name':match[1], 'age':match[2], 'city':match[3]} for match in matches]
print(data)



# val = [x for x in range(10)]
# print(val)


# val = []
# for x in range(10):
#     val.append(x)

# csv_file = open(r"C:\python-works\python_works\student_grades.csv", mode='rt')

# data = csv_file.read()

# matches = re.findall(r'(\w+) (\w+),(\d+),(\w)', data)
# print(matches)

# student_details = [{'First Name': each[0], 'Last Name':each[1], 'Score': each[2], 'Grade':each[3]} for each in matches]
# print(student_details)

# user = input('password: ')
# pattern = ['a-bA-Z']

# 3. You can use regex to validate the strength of passwords based on specific criteria
# 4. You can use regex to remove HTML tags from a string and extract the plain text content
# 5. You can use regex to extract hashtags from a text or social media content
# 6. You can use regex to validate URLs and ensure they follow a specific format