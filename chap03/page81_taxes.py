#!/usr/local/bin/python3.7

while True:
    income = float(input("What is your salary:") )
    if income == 0:
        break
    if income < 10000:
        tax_coefficient = 0.0 #1
    elif income < 30000:
        tax_coefficient = 0.2 #2
    elif income < 100000:
        tax_coefficient = 0.35 #3
    else:
        tax_coefficient = 0.45 #4

    print('I will pay:', income * tax_coefficient, 'in taxes')
    print('Enter 0 to finish, or give another income.')


