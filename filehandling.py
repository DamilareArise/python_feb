
#File-Hanling

# myfile = open(r'C:\python_feb\while_loop.py') 
# print(myfile)

# mode
'''
r - read only
w - write
a - append
x - create
'''

# myfile = open(r'C:\python_feb\myfile.txt') 
# print(myfile.read())
# print(myfile.readlines())

# x = 0
# for line in myfile.readlines():
#     print(line)
#     if x == 5:
#         break
#     x += 1
# myfile.close()

# with open(r'C:\python_feb\myfile.txt', encoding='utf-8') as file:
#     print(file.read())

# file.read()

# with open(r"C:\Users\Hp\Desktop\ROBOTICS IGNITION 1.docx", mode='rt', encoding='utf-8') as file:
#     print(file.read())

# myfile = open('C:\\python_feb\\myfile2.csv', mode='x')


# with open('C:\python_feb\myfile2.txt', mode='wt') as myfile:
#     myfile.write('Hello world...')


# with open('C:\python_feb\myfile2.txt', mode='a') as myfile:
#     myfile.write('Hello world...\n')
    
import os
# os.mkdir(r'C:\python_feb\newfolder')
# os.rmdir(r'C:\python_feb\newfolder')
# os.remove(r'C:\python_feb\myfile2.txt')
# print(os.path.exists(r'C:\python_feb\myfile2.txt'))

# print(os.walk("C:\python_feb"))
for root, folder, file in os.walk(r"C:\python_feb\newDIR"):
    print( root, folder, file)


# if os.path.exists("C:\python_feb\\text2.pdf"):
#     print('File exist')
#     print('-'*98)
#     with open("C:\python_feb\\text2.pdf", mode="rt") as myFile:
#         print(myFile.read())
# else:
#     print("file does not exists")
#     print('_'*98)
#     with open("C:\python_feb\\text2.pdf", "xt") as myFile:
#         print("file created successfully")

# if os.path.exists("C:\python_feb\\text2.pdf"):
#     os.remove("C:\python_feb\\text2.pdf")
#     print("file deleted ")
# else:
#     print("file not available")


# TASK1

# Creating a directory with os module

# os.mkdir("C:\python_feb\\newDIR")
# file = open('C:\python_feb\\newDIR\\text.py', mode='x')
# file = open('C:\python_feb\\newDIR\\text.csv', mode='x')

# print('Folder and files created successfully')

# os.rmdir(r'C:\python_feb\\newDIR')
# # Deleting a directory

import time

# try:
#     os.rmdir("C:\python_feb\\newDIR")
# except OSError:
#     print('The folder is not empty')
#     for root, folder, files in os.walk("C:\python_feb\\newDIR"):
#         print(files)

#         for file in (files):
#             print('Deleting', file)
#             time.sleep(2)
#             os.remove("C:\python_feb\\newDIR\\"+file)

#     print('Deleting Directory')
#     time.sleep(1)
#     os.rmdir("C:\python_feb\\newDIR")

# TASK2

# os.mkdir("C:\python_feb\\ROOTDIR")
# os.mkdir("C:\python_feb\\ROOTDIR\\DIR1")

# file = open('C:\python_feb\\ROOTDIR\\text.py', mode='x')
# file = open('C:\python_feb\\ROOTDIR\\DIR1\\text.csv', mode='x')

# for file in os.walk('C:\python_feb\\ROOTDIR'):
#     # print(root)
#     # print(folder)
#     print(file)