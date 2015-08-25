# Develop a program that can generate one's
# budget based on their pay.


income = float(input('What did you get paid?\n$'))

savings = income*(0.10)
tithe = income*(0.10)
personalUse = income*(0.10)
bills = income*(0.55)
investments = income*(0.10)
myMoney = income*(0.05)

total = (savings+tithe+personalUse+bills+investments+myMoney)


if income < 2224:
    print("\tSavings\tTithe\tP.Use\tBills\tInvsts\tMy $")
    print("\t-------\t-------\t-------\t-------\t-------\t-------")
    print("\t$%.2f\t$%.2f\t$%.2f\t$%.2f\t$%.2f\t$%.2f" %(savings,tithe,personalUse,bills,investments,myMoney))
elif income > 2224 and income < 5000:
    print("\tSavings\t\tTithe\t\tP.Use\t\tBills\t\tInvsts.\t\tMy $")
    print("\t--------\t--------\t--------\t--------\t--------\t--------")
    print("\t$%.2f\t\t$%.2f\t\t$%.2f\t\t$%.2f\t$%.2f\t\t$%.2f" %(savings,tithe,personalUse,bills,investments,myMoney))
elif income > 5000 and income < 10000:
    print("\tSavings\t\tTithe\t\tP.Use\t\tBills\t\tInvsts.\t\tMy $")
    print("\t--------\t--------\t--------\t--------\t--------\t--------")
    print("\t$%.2f\t\t$%.2f\t\t$%.2f\t$%.2f\t$%.2f\t\t$%.2f" %(savings,tithe,personalUse,bills,investments,myMoney))
elif income > 10000 and income < 250001:
    print("\tSavings\t\tTithe\t\tP.Use\t\tBills\t\tInvsts.\t\tMy $")
    print("\t--------\t--------\t---------\t---------\t--------\t--------")
    print("\t$%.2f\t$%.2f\t$%.2f\t$%.2f\t$%.2f\t$%.2f" %(savings,tithe,personalUse,bills,investments,myMoney))
    
#if income != total:
#    print("Your income doesn't match your total money earned.")

