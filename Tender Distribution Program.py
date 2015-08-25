# Tender Distribution Program

tender = ['Hundreds','Fifties','Twenties','Tens','Fives','Twos','Ones','Half-Dollars','Quarters','Dimes','Nickles','Pennies']
tenderIndex = len(tender)-1
quantity = [100,50,20,10,5,2,1,0.5,0.25,0.10,0.05,0.01]
i = 0

money = input('\nHow much money do you have?\n|-> $')

#Test condition
try:
        yourMoney = float(money)
except (ValueError)as error:
        print('\nYou can only enter numbers here:\n(%s)' % error)
else:
        print('\n\tOkay nice!')


print('\nHere are your options: \n')
#Show money 
while i <= tenderIndex:
	print('\t',tender[i],'- $%.2f'%(quantity[i]))
	i += 1

#Choice
if yourMoney >= quantity[0]:
        
        H = input('\nHow many hundreds do you want? \n::: ')
        try: hundreds = float(H)
        except (ValueError)as error:
                print('\nYou can only enter whole numbers here:\n(%s)' % error)
        else:
                if (hundreds*100) > yourMoney:
                        print("Sorry, you don't have enough money. Choose a different value.")
                else:
                        hundreds = hundreds * quantity[0]
                        
        F = input('How many fifties do you want? \n::: ')
        try: fifties = float(F)
        except (ValueError)as error:
                print('\nYou can only enter whole numbers here:\n(%s)' % error)
        else:
                if (fifties*50) > yourMoney:
                        print("Sorry, you don't have enough money. Choose a different value.")
                else:
                        fifties = fifties * quantity[1]

        T = input('How many twenties do you want? \n::: ')
        try: twenties = float(T)
        except (ValueError)as error:
                print('\nYou can only enter whole numbers here:\n(%s)' % error)
        else:
                if (twenties*20) > yourMoney:
                        print("Sorry, you don't have enough money. Choose a different value.")
                else:
                        twenties = twenties * quantity[2]

        N = input('How many tens do you want? \n::: ')
        try: tens = float(N)
        except (ValueError)as error:
                print('\nYou can only enter whole numbers here:\n(%s)' % error)
        else:
                if (tens*10) > yourMoney:
                        print("Sorry, you don't have enough money. Choose a different value.")
                else:
                        tens = tens * quantity[3]

        V = input('How many fives do you want? \n::: ')
        try: fives = float(V)
        except (ValueError)as error:
                print('\nYou can only enter whole numbers here:\n(%s)' % error)
        else:
                if (fives*5) > yourMoney:
                        print("Sorry, you don't have enough money. Choose a different value.")
                else:
                        fives = fives * quantity[4]

        W = input('How many twos do you want? \n::: ')
        try: twos = float(W)
        except (ValueError)as error:
                print('\nYou can only enter whole numbers here:\n(%s)' % error)
        else:
                if (twos*2) > yourMoney:
                        print("Sorry, you don't have enough money. Choose a different value.")
                else:
                        twos = twos * quantity[5]

        O = input('How many ones do you want? \n::: ')
        try: ones = float(O)
        except (ValueError)as error:
                print('\nYou can only enter whole numbers here:\n(%s)' % error)
        else:
                if ones > yourMoney:
                        print("Sorry, you don't have enough money. Choose a different value.")
                else:
                        ones = ones * quantity[6]

        total = (hundreds + fifties + twenties + tens + fives + twos + ones)

        if total == yourMoney:
                #Make Tender Trace Table
                print("\n\tMoney Distribution:\n\t-------------------------------------------------------------------------------------------")
                print('\t',"%d's | %d's | %d's | %d's | %d's | %d's | %d's | %.2f's | %.2f's | %.2f's | %.2f's | %.2f's" % (quantity[0],quantity[1],quantity[2],quantity[3],quantity[4],quantity[5],quantity[6],quantity[7],quantity[8],quantity[9],quantity[10],quantity[11]))
                print("\t-------------------------------------------------------------------------------------------")
                print('\t',"$%d  |$%d  |$%d  |$%d  |$%d  |$%d  |$%d  |$%.2f's |$%.2f's |$%.2f's |$%.2f's |$%.2f's" % (hundreds,fifties,twenties,tens,fives,twos,ones,quantity[7],quantity[8],quantity[9],quantity[10],quantity[11]))
        else:
                print('Sorry, you failed to meet the requirements. Try again.')
                        
#elif yourMoney < quantity[0] and yourMoney >= quantity[1]:

#elif yourMoney < quanitiy[1] and yourMoney >= quantity[2]:

#elif yourMoney < quanitiy[2] and yourMoney >= quantity[3]:

#elif yourMoney < quanitiy[3] and yourMoney >= quantity[4]:

#elif yourMoney < quanitiy[4] and yourMoney >= quantity[5]:

#elif yourMoney < quanitiy[5] and yourMoney >= quantity[6]:
        
else:
        print("You have to withdraw at least a dollar.\n\tTry again.")  
