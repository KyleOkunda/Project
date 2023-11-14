pin = 2023
balance = 250000
while True:
    
    
    request = int(input('''
1. Send money
2. Withdraw cash
3. Buy airtime
4. Lipa na Mpesa
5. My account
6. Exit \n'''))

    if request == 1:
        receiver = input('Enter phone Number: \n')
        if receiver[0:4] == '+254':
            receiver = receiver.replace('+254','0')

        if receiver[0:2] != '07' or len(receiver) != 10:
            print('Invalid output')
        else:
            amount = int(input('Enter amount: \n'))
            verification = int(input('Enter pin: \n'))
            balance -= amount
            if verification == pin:
                print(f'Send Ksh {amount} to {receiver}.')
                print(f'New balance is {balance}')
            else:
                print('Incorrect pin')

    elif request == 2:
        agent = input('Enter Agent Number: \n')
        if len(agent) != 6:
            print('Invalid Agent Number')
        else:
            store_no = input('Enter store number: \n')
            if len(store_no) != 6:
                print('Invalid store number.')
            else:
                amount = int(input('Enter amount: \n'))
                verification = int(input('Enter pin: \n'))
                balance -= amount
                if verification == pin:
                    print(f'{amount} withdrawn from agent {agent} with store number {store_no}')
                    print(f'New balance is {balance}')
                else: 
                    print('Invalid pin')

    elif request == 3:
        query = input('''
a. My phone
b. Other phone \n''').lower()
        if query == 'a':
            amount = int(input('Enter amount: \n'))
            verification = int(input('Enter pin: \n'))
            balance -= amount
            if verification == pin:
                print(f'Bought {amount} airtime.')
                print(f'New balance is {balance}')
            else:
                print('Invalid pin')
        elif query == 'b':
            receiver = input('Enter phone Number: \n')
            if receiver[0:4] == '+254':
                receiver = receiver.replace('+254','0')
            if receiver[0:2] != '07' or len(receiver) != 10:
               print('Invalid output')
            amount = int(input('Enter amount: \n'))
            verification = int(input('Enter pin: \n'))
            balance -= amount
            if verification == pin:
                print(f'Bought {amount} airtime for {receiver}.')
                print(f'New balance is {balance}')
            else: 
             print('Invalid pin')
    elif request == 4:
        query = input('''
a. Pay bill
b. Buy goods and services
c. Pochi                                     \n''').lower()
        if query == 'a':
            business = input('Enter business number: \n')
            if len(business) != 6 :
                print('Invalid business number.')
            else:
                account = input('Enter account number: \n')
                if len(account) != 6:
                    print('Invalid account number.')
                else:
                    amount = int(input('Enter amount: \n'))
                    verification = int(input('Enter pin: \n'))
                    balance -= amount
                    if verification == pin:
                        print(f'Ksh {amount} paid to businiess number {business} for account {account}.')
                        print(f'New balance is {balance}')
                    else:
                        print('Invalid pin.')
        elif query == 'b':
            till = input('Enter Till number: \n')
            if len(till) != 6:
                print('Invalid Till number.')
            else:
                amount = int(input('Enter amount: \n'))
                verification = int(input('Enter pin: \n'))
                balance -= amount
                if verification == pin:
                    print(f'Ksh {amount} paid to Till number {till}.')
                    print(f'New balance is {balance}')
                else:
                    print('Invalid pin.')
        elif query == 'c':
            receiver = input('Enter phone Number: \n')
            if receiver[0:4] == '+254':
              receiver = receiver.replace('+254','0')
            if receiver[0:2] != '07' or len(receiver) != 10:
               print('Invalid output')
            else:
               amount = int(input('Enter amount: \n'))
               verification = int(input('Enter pin: \n'))
               balance -= amount
               if verification == pin:
                   print(f'Ksh {amount} paid to {receiver}.')
                   print(f'New balance is {balance}')
               else:
                    print('Invalid pin')
        else:
            print('Invalid entry.')
    
    elif request == 5:
        query = input('''
a. Check balance
b. Change pin                   \n''')
        if query == 'a':
            print(balance)
        elif query == 'b':
            new = int(input('Enter new pin: '))
            confirm = int(input('Confirm new pin: '))
            if new != confirm:
                print('The two do not match.')
            else:
                print(f'The new pin is {new}')
                pin = new
        else:
            print('Invalid entry.')
    elif request == 6:
        break
    else:
        print('Invalid entry.')
   
        

        