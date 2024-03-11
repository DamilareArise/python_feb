students_db = [
    ('Tolu','Paid'),
    ('Maimunat', 'Half-paid'),
    ('Habeeb','No-paid')

]

staff_db = [
    ('Femi', '21'),
    ('Yemi', '02')
]


user = input('''
            Welcome to SQI Colleg Of ICT
    
    Kindly clarify your identity
    1. Staff
    2. Student
    3. Visitor
    4. None of the above

    option: ''').strip()

if user == '1' or user.capitalize() == 'Staff':
    staff_id = input('ID: ').strip()
    staff_fname = input('First name: ').strip().capitalize()

    fnames = []
    IDs = []

    for fname, id in staff_db:
        fnames.append(fname)
        IDs.append(id)

    
    if staff_fname in fnames and staff_id in IDs:
        print('Access granted😁')
    else:
        print('Access denied!')
    
elif user == '2' or user.capitalize() == 'Student':
    student_fname = input('First name: ').strip().capitalize()
 
    student_firstnames = []
    payment_status = []

    for stud, status in students_db:
        student_firstnames.append(stud)
        payment_status.append(status)

    if student_fname in student_firstnames:
        print(f'Welcome {student_fname}, Kindly wait, lets verify your payment status')

        _index = student_firstnames.index(student_fname)
        _status = payment_status[_index]
        # print(_status)

        if _status == 'Paid':
            print(f'Great, Welcome to class {student_fname}')
        else:
            print(f"{student_fname}, Your payment status is '{_status}', Kindly visit the frontdesk for clarification.")
    else:
        print('Record not found, Try agian or visit the frontdesk')

# print('''
#     Thanks Mr Dami, your Order are;
#     1. Nike Sneakers --> #20000
#     2. Rolex --> #30000
    
#     Total = #50000
#     ''')