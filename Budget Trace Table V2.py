'''
Budget Trace Table.py
Problem: Calculate someone's budget into categories.
Target Users: Anyone who wants to manage their money by creating a budget.
Target System: GNU/Linux/Windows/MacOS
Interface: Command-line
Functional Requirements:
    - User must input the percentage for each category.
    - The percentages should not exceed 1.00 or 100%.
    - Tell the user how much interest they put in as they enter values.
    - Create Trace Table to track categories & calculations.
Testing: Simple run test
Creator: Notorious Scott
version = 0.2
'''


income = float(input('What did you get paid?\n$'))

while True:
    while True:
        savingsPer = int(input('\nWhat percentage of your income goes to savings?\n'))
        total = savingsPer
        print('You have %d left' % (100 - total))

        tithePer = int(input('What percentage of your income goes to tithe?\n'))
        total = tithePer + total
        print('You have %d left' % (100 - total))

        personalUsePer = int(input('What percentage of your income goes to personal use?\n'))
        total = personalUsePer + total
        print('You have %d left' % (100 - total))

        billsPer = int(input('What percentage of your income goes to bills?\n'))
        total = billsPer + total
        print('You have %d left' % (100 - total))

        investmentsPer = int(input('What percentage of your income goes to investments?\n'))
        total = investmentsPer + total
        print('You have %d left' % (100 - total))

        myMoneyPer = int(input('What percentage of your income goes to your spending money?\n'))
        total = myMoneyPer + total
        print('You have %d left' % (100 - total))
        break

    if total == 100:
        savings = income*savingsPer*(0.01)
        tithe = income*tithePer*(0.01)
        personalUse = income*personalUsePer*(0.01)
        bills = income*billsPer*(0.01)
        investments = income*investmentsPer*(0.01)
        myMoney = income*myMoneyPer*(0.01)
        break
    elif total > 100:
        print('The total percentages of the categories exceeds 100%. Please re-enter the values')
        continue
    elif total < 100:
        print('The total percentages of the categories is less than 100%. Please re-enter the values')
        continue
    

total = (savings+tithe+personalUse+bills+investments+myMoney)


if income < 2224:
    print("\n\n\tSavings\tTithe\tP.Use\tBills\tInvsts\tMy $")
    print("\t-------\t-------\t-------\t-------\t-------\t-------")
    print("\t$%.2f\t$%.2f\t$%.2f\t$%.2f\t$%.2f\t$%.2f" %(savings,tithe,personalUse,bills,investments,myMoney))
elif income < 5000:
    print("\n\n\tSavings\t\tTithe\t\tP.Use\t\tBills\t\tInvsts.\t\tMy $")
    print("\t--------\t--------\t--------\t--------\t--------\t--------")
    print("\t$%.2f\t\t$%.2f\t\t$%.2f\t\t$%.2f\t$%.2f\t\t$%.2f" %(savings,tithe,personalUse,bills,investments,myMoney))
elif income < 10000:
    print("\n\n\tSavings\t\tTithe\t\tP.Use\t\tBills\t\tInvsts.\t\tMy $")
    print("\t--------\t--------\t--------\t--------\t--------\t--------")
    print("\t$%.2f\t\t$%.2f\t\t$%.2f\t$%.2f\t$%.2f\t\t$%.2f" %(savings,tithe,personalUse,bills,investments,myMoney))
elif income < 250001:
    print("\n\n\tSavings\t\tTithe\t\tP.Use\t\tBills\t\tInvsts.\t\tMy $")
    print("\t--------\t--------\t---------\t---------\t--------\t--------")
    print("\t$%.2f\t$%.2f\t$%.2f\t$%.2f\t$%.2f\t$%.2f" %(savings,tithe,personalUse,bills,investments,myMoney))
    
#if income != total:
#    print("Your income doesn't match your total money earned.")

