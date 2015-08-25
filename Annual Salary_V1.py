# Total Annual Salary

def annual_salary():
    print("\nWhat is your total annual salary? ")
    salary = float(input('$'))
    weeks = 52
    hoursWorked = weeks * 40
    hourlyWage = salary/hoursWorked
    print('Your hourly wage is: $%.2f' % (hourlyWage))

def hourly_salary():
    print("\nHow much do you make an hour? ")
    wages = float(input('$'))
    weeks = 52
    hoursWorked = weeks * 40
    salary = hoursWorked*wages
    print('Your annual salary is: $%.2f' % (salary))

choice = input('\nDo you want to check your Annual Salary(A) or your hourly Wages(W)? (A/W)\n')
choiceType = type(choice)

while True:
    if choice == 'A' or choice == 'a':
        hourly_salary()

        r = input("\nTry another salary(Y/N)? ")

        if r == 'Y':
            hourly_salary()

        else:
            if r == 'N':
                print("\nOkay great!")
                break

    elif choice == 'W':
        annual_salary()

        r = input("\nTry another salary(Y/N)? ")

        if r == 'Y':
            annual_salary()

        else:
            if r == 'N':
                print("\nOkay great!")
                break

    else:
        print('(Case Sensitive) Only enter A or W for an answer. Try again.\n')
        break
print("Thank you for using Hourly Wages services!")



# Test condition
# if type(salary) != "<class 'str'>":
#   print ('''\nYOU CAN ONLY ENTER WHOLE OR RATIONAL NUMBERS!!!
#            Try again please.''')



