import random
import BankApp

def register():
    db = open("authentication.txt", "r") #read db authentication.txt
    username = input("Create username: ")
    password = input("Create password: ")
    password1 = input("Re-enter password: ")
    u = []
    p = []
    for i in db:
        j, k = i.split(", ")
        k = k.strip()
        u.append(j)
        p.append(k)
    login = dict(zip(u, p))
    #This statement will not accept if the password dont match
    if password != password1:
        print("Password don't match.")
        register()
    #The statement below limit password to 6 characters and cannot use the same username
    else:
        if len(password) <= 6:
            print("Password too short. Password should contain more than 6 characters.")
            register()
        elif username in u:
            print("Username is taken. Please use a different username.")
            register()
        else:
            db = open("authentication.txt", "a")
            db.write(username + ", " + password + "\n") #write values to the db authentication.txt
            print("Successfully created an account.")

if __name__ == "__main__":
    register()

#This function will verify if the username is in db authentication.txt
def access():
    db = open("authentication.txt", "r")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not len(username or password) < 1:
        u = []
        p = []
        for i in db:
            j, k = i.split(", ")
            k = k.strip()
            u.append(j)
            p.append(k)
        login = dict(zip(u, p))

        if login[username]:
            if password == login[username]:
                print("Login success.")
                print("\n")
                print("Hi", username + "!")
                choice()
            else:
                print("Incorrect username or password.")
                access()

#Need to work on adding the details in the database so it will tied on the user created above
def choice():
    # db = open("acct_details.txt", "r")
    acctnumber = ['1234567', '1357911', '2468101', '3691215', '4812162']
    pincode = ['1234', '1357', '2468', '3691', '4812']
    balance = [1000, 500, 100, 2000, 3000]
    deposit = 0
    withdrawal = 0
    bal = 0
    counter1 = 1
    counter2 = 5 #limit the number of accounts to 5
    n = 0

    #This statement will run continously.
    while True:
        print("==============================")
        print("|What would you like to do?  |")
        print("==============================")
        print("== [1] Create Account       ==")
        print("== [2] Balance              ==")
        print("== [3] Deposit              ==")
        print("== [4] Withdrawal           ==")
        print("== [5] Go to other account  ==")
        print("== [6] Exit                 ==")
        print("==============================")
        selection = input("Enter the number you wish to do: ")
        #This statement will execute the selection of customer from [1]-[6] option.
        if selection == "1":
            print("You choice is [1] Create Account"+"\n")
            numberCust = eval(input("Enter number of accounts you wish to enter: "))
            n = n + numberCust
            #This statement will prompt when you reached 5 accounts.
            if n > 5:
                print("\n" + "You have reached the maximum accounts per customer.")
                n = n - numberCust
            else:
                #This will run depending on the input in number of customer, I set max:5
                while counter1 <= n:
                    #Input of Customer Information
                    acct = input("Enter account number: ")
                    acctnumber.append(acct)
                    pin = input("Enter pin code: ")
                    pincode.append(pin)
                    bal = 0
                    deposit = eval(input("Enter the desired amount you want to deposit: "))
                    bal = bal + deposit
                    balance.append(bal)
                    print("Balance=", end=" ")
                    counter1 = counter1 + 1
                    print(acctnumber[counter2])
                    print("Pin=", end=" ")
                    print(pincode[counter2])
                    print("Balance=", end=" ")
                    print(balance[counter2], end=" ")
                    counter1 = counter1 + 1
                    counter2 = counter2 + 1
                    # db = open("acct_details.txt", "a")
                    # db.write(acct + ", " + str(bal) + ", " +str(deposit)+"\n")
                    print("\n"+"You have successfully created an account and added on the list.")
                    print(acctnumber)
                    print(balance)
                choice()
        elif selection == "2":
            print("You choice is [2] Check Balance"+"\n")
            a = 0
            while a < 1:
                b = -1
                acct = input("Please enter account number: ")
                pin = input("Please enter pin code : ")
                # The while loop below will keep the function running to find the correct user.
                while b < len(acctnumber) - 1:
                    b = b + 1
                    # The two if conditions below would find whether both the pin and the name is correct.
                    if acct == acctnumber[b]:
                        if pin == pincode[b]:
                            a = a + 1
                            print("Your Current Balance: ", end=" ")
                            print(balance[b], end=" ")
                            print("\n")
                            bal = (balance[b])
                            balance[b] = bal
                            print("\n")
                if a < 1:
                    print("Your account number and pin does not match!\n")
                    break
        elif selection == "3":
            print("You choice is [3] Deposit " + "\n")
            o = 0
            # The while loop below will not work when the pin or the username is wrong.
            while o < 1:
                p = -1
                acct = input("Please enter account number: ")
                pin = input("Please enter pin code : ")
                # The while loop below will keep the function running to find the correct user.
                while p < len(acctnumber) - 1:
                    p = p + 1
                    # The two if conditions below would find whether both the pin and the name is correct.
                    if acct == acctnumber[p]:
                        if pin == pincode[p]:
                            o = o + 1
                            # These statements below would show the account balance and update list values according to
                            # the deposit made.
                            print("Your Current Balance: ", end=" ")
                            print(balance[p], end=" ")
                            print("\n")
                            bal = (balance[p])
                            # This statement below record the deposit from the account.
                            deposit = eval(input("Enter the value you want to deposit : "))
                            bal = bal + deposit
                            balance[p] = bal
                            print("\n")
                            print("Amount has been added to your account.")
                            print("Account number: " + acct, end=" ")
                            print("\n")
                            print("Your New Balance: ", bal, end=" ")
                            print("\n")
                if o < 1:
                    print("Your account number and pin does not match!\n")
                    break
        elif selection == "4":
            print("You choice is [4] Withdrawal"+"\n")
            q = 0
            # This while loop will prevent the user using the account if the username or pin is wrong.
            while q < 1:
                r = -1
                acct = input("Please enter acccount number: ")
                pin = input("Please enter pin: ")
                # This while loop will keep the function running when variable r is smaller than length of the account list.
                while r < len(acctnumber) - 1:
                    r = r + 1
                    # These two if conditions find where both the account and pin matches.
                    if acct == acctnumber[r]:
                        if pin == pincode[r]:
                            q = q + 1
                            # These statement would show the balance from the list.
                            print("Your Current Balance:", end=" ")
                            print(balance[r], end=" ")
                            bal = (balance[r])
                            #Statement below would take the amount to withdraw from user.
                            withdrawal = eval(input("\n"+"Enter amount to Withdraw : "))
                            #The if condition will not accept if withdrawn are greater than the available balance
                            if withdrawal > bal:
                                #This statement below will evaluate deposit from the customer
                                deposit = eval(input("Insufficient balance..."))
                                #These statements show and update customer balance
                                bal = bal + deposit
                                print("Your Current Balance:", end=" ")
                                print("\n")
                                print(bal, end=" ")
                                bal = bal - withdrawal
                                print("\n")
                                print("Withdrawal Successful."+"\n")
                                balance[r] = bal
                                print("Your New Balance: ", balance, end=" ")
                                print("\n")
                            else:
                                # amount withdrawn
                                bal = bal - withdrawal
                                # These few statement would update the values in the list and show it to the account.
                                print("\n")
                                print("Withdrawal Successful.")
                                balance[r] = bal
                                print("Your New Balance: ", bal, end=" ")
                                print("\n")
                if q < 1:
                    # The if condition determine if account number or pin is wrong.
                    print("Account number or pin is incorrect!\n")
                    break
        elif selection == "5":
            print("You choice is [5] Go to other account/s" + "\n")
            m = 0
            print("Below are the list of customer account number and balances: ")
            print("\n")
            # Continuous run until all the customers and balances are appear.
            while m <= len(acctnumber) - 1:
                print("Account number =", acctnumber[m])
                print("Balance =", balance[m], end=" ")
                print("\n")
                m = m + 1
        #This function will end the program.
        elif selection == "6":
            exit()
        else:
            choice()



