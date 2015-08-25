#!/usr/bin/env python 3.2

def annual_salary():
    print("\nWhat is your total annual salary? ")
    s = input('$')
    try:
        salary = float(s)
    except (ValueError)as error:
        print('\nYou cannot use a string here! Only numbers:\n(%s)' % error)
    else:
        weeks = 52
        hoursWorked = weeks * 40
        hourlyWage = salary/hoursWorked
        biWeekly = hourlyWage * 80
        print('''Your hourly wage is: $%.2f

Biweekly rate is:
$%.2f''' % (hourlyWage,biWeekly))

def hourly_salary():
    print("\nHow much do you make an hour? ")
    w = input('$')
    try:
        wages = float(w)
    except (ValueError)as error:
        print('\nYou cannot use a string here! Only numbers:\n(%s)' % error)
    else:
        weeks = 52
        hoursWorked = weeks * 40
        salary = hoursWorked*wages
        biWeekly = salary/26
        print('''Your hourly wage is: $%.2f

Biweekly rate is:
$%.2f''' % (salary,biWeekly))


while True:
    choice = input('''\n\t*** Type Quit or q to stop the program ***\n\n
Do you want to check your Annual Salary(A) or your Hourly Wages(W)? (A/W)\n''')

    if choice == 'quit' or choice == 'Quit' or choice == 'q':
        break

    while True:
        if choice == 'A' or choice == 'a':
            hourly_salary()

            retry = input("\nTry again(Y/N)? ")

            if retry == 'Y' or retry == 'y':
                continue
            elif retry == 'N' or retry == 'n':
                break
            continue

        elif choice == 'W' or choice == 'w':
            annual_salary()

            retry = input("\nTry again(Y/N)? ")

            if retry == 'Y' or retry == 'y':
                continue
            elif retry == 'N' or retry == 'n':
                break
            continue

        else:
            print('Follow the instructions: Try again.\n')
            break
        continue
    
print("Thank you for using Hourly Wages services!")





