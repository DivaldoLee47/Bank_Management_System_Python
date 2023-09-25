#DIVALDO LEE
#TP062988 

import datetime as systemDateTime

#--------------------------------------------------------------------------------------------------------------------------------
# DATETIME CHECKER

def accDateTime():
    currentDateTime = systemDateTime.datetime.now()
    currentDateTime = currentDateTime.strftime(" on %d/%m/%Y at %H:%M:%S")
    dateOnly = systemDateTime.datetime.now()
    dateOnly = dateOnly.strftime("%d/%m/%Y")
    return(currentDateTime, dateOnly)

#--------------------------------------------------------------------------------------------------------------------------------
# STATEMENT ACCOUNT REPORT

def statementAccReport(accBalance, amount, accNum, performType, newAccBalance1, newAccBalance2, transferAccDest, accBalanceDest):
    date, dateOnly = accDateTime()
    file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\transactionreport.txt","a")
    if performType == "deposit":
        file.write(f"{accNum}|Deposit of RM {amount} SUCCESS! Balance Updated From {accBalance} ==> {newAccBalance1}{date}|{dateOnly} \n")
    elif performType == "withdrawal":
        file.write(f"{accNum}|Withdrawal of RM {amount} SUCCESS! Balance Updated From {accBalance} ==> {newAccBalance1}{date}|{dateOnly} \n")
    elif performType == "transfer":
        file.write(f"{accNum}|Transfer of RM {amount} to {transferAccDest} SUCCESS! Balance Updated From {accBalance} ==> {newAccBalance1}{date}|{dateOnly} \n")
        file.write(f"{transferAccDest}|Received Transfer of RM {amount} from {accNum} SUCCESS! Balance Updated From {accBalanceDest} ==> {newAccBalance2}{date}|{dateOnly} \n")
    file.close()
    return(accNum)

#--------------------------------------------------------------------------------------------------------------------------------
# CUSTOMER GENERATE ACCOUNT REPORT

def generateReport(accNum):
    dateValid = False
    while not dateValid:
        error = False
        beginDate = input("Enter The Starting Date Range To Generate Statement Account Report [dd/mm/yyyy]: \n")
        endDate = input("Enter The End Date Range To Generate Statement Account Report [dd/mm/yyyy]: \n")
        print("\n               STATEMENT OF ACCOUNT " + "[" + accNum + "]" + " REPORT")
        print("--------------------------------------------------------------\n")
        file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\transactionreport.txt", "r")
        for rec in file:
            acc = rec.split("|")
            if accNum == acc[0]:
                accDate = acc[2]
                try:
                    if int(beginDate.split("/")[2]) <= int(endDate.split("/")[2]):
                        if int(beginDate.split("/")[2]) == int(accDate.split("/")[2]) or int(endDate.split("/")[2]) == int(accDate.split("/")[2]):
                            if (int(beginDate.split("/")[1]) <= int(endDate.split("/")[1])) and (int(beginDate.split("/")[1]) < 13) and (int(endDate.split("/")[1]) < 13):
                                if int(beginDate.split("/")[1]) == int(accDate.split("/")[1]) and int(endDate.split("/")[1]) == int(accDate.split("/")[1]):
                                    if (int(accDate.split("/")[0]) > int(beginDate.split("/")[0])) and (int(accDate.split("/")[0]) < int(endDate.split("/")[0])):
                                        print(str(acc[1]))
                                        dateValid = True
                                    elif (int(accDate.split("/")[0]) > int(beginDate.split("/")[0])) and (int(accDate.split("/")[0]) == int(endDate.split("/")[0])):
                                        print(str(acc[1]))
                                        dateValid = True
                                    elif (int(accDate.split("/")[0]) == int(beginDate.split("/")[0])) and (int(accDate.split("/")[0]) < int(endDate.split("/")[0])):
                                        print(str(acc[1]))
                                        dateValid = True
                                    elif (int(accDate.split("/")[0]) >= int(beginDate.split("/")[0])) and (int(accDate.split("/")[0]) <= int(endDate.split("/")[0])):                             
                                        print(str(acc[1]))
                                        dateValid = True

                                elif (int(accDate.split("/")[1]) > int(beginDate.split("/")[1])) and (int(accDate.split("/")[1]) < int(endDate.split("/")[1])):
                                    print(str(acc[1]))
                                    dateValid = True

                                elif (int(accDate.split("/")[1]) > int(beginDate.split("/")[1])) and (int(accDate.split("/")[1]) == int(endDate.split("/")[1])):
                                    if (int(accDate.split("/")[0]) <= int(endDate.split("/")[0])):
                                        print(str(acc[1]))
                                        dateValid = True

                                elif (int(accDate.split("/")[1]) == int(beginDate.split("/")[1])) and (int(accDate.split("/")[1]) < int(endDate.split("/")[1])):
                                    if (int(accDate.split("/")[0]) >= int(beginDate.split("/")[0])):
                                        print(str(acc[1]))
                                        dateValid = True

                        elif (int(accDate.split("/")[2]) > int(beginDate.split("/")[2])) and (int(accDate.split("/")[2]) < int(endDate.split("/")[2])):
                            print(str(acc[1]))
                            dateValid = True

                except IndexError:
                    print("Please Enter The Correct Format!")
                    error = True
                    break
        
        if not dateValid and not error:
            print("No Transaction Found!")

    return(accNum) 
#--------------------------------------------------------------------------------------------------------------------------------
# TRANSFER REQUIREMENTS

def transferRequirement(transferAccDest, accBalance, accBalanceDest, transferAmount, accNum, minBal, count1, count2, acc, acc2, performType):
    if accBalance <= minBal:
        print("\nTransfer Request DENIED.")
        print("PS: Current Balance Under Minimum Requirement (RM" + str(minBal) + ") !\n"
                "Current Balance: " + str(accBalance) + "\n"
                "\nBack to Home Page")
        customerMenu(accNum)

    elif accBalance > minBal:
        notRoundedAvalBal = accBalance - minBal
        availableBalance = round(notRoundedAvalBal, 2)
        if transferAmount > availableBalance:
            print("\nTransferl Request DENIED.\n"
                "Transfer Amount Exceeds Minimum Balance! ... Please Try Again.\n"
                "\nCurrent Available Balance For Transfer/Withdrawal: RM" + str(availableBalance) + "\n")

        elif transferAmount <= availableBalance:
            notRoundedBal1 = accBalance - transferAmount
            newAccBalance1 = round(notRoundedBal1, 2)

            file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
            newRec1 = file.readlines()
            
            newRec1[count1] = f"{acc[0]}:{acc[1]}:{acc[2]}:{acc[3]}:{acc[4]}:{acc[5]}:{acc[6]}:{acc[7]}:{acc[8]}:{newAccBalance1}\n"

            file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","w")
            file.writelines(newRec1)
            file.close()

            notRoundedBal2 = accBalanceDest + transferAmount
            newAccBalance2 = round(notRoundedBal2, 2)

            file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
            newRec2= file.readlines()
            
            newRec2[count2] = f"{acc2[0]}:{acc2[1]}:{acc2[2]}:{acc2[3]}:{acc2[4]}:{acc2[5]}:{acc2[6]}:{acc2[7]}:{acc2[8]}:{newAccBalance2}\n"

            file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","w")
            file.writelines(newRec2)
            file.close()
            
            print("\nTRANSFER to " + str(transferAccDest) + " Success!\n")
            print("Your Current Balance: RM" + str(newAccBalance1))

            statementAccReport(accBalance, transferAmount, accNum, performType, newAccBalance1, newAccBalance2, transferAccDest, accBalanceDest)
            
            return(accNum)

#--------------------------------------------------------------------------------------------------------------------------------
# TRANSFER PAGE

def custTransfer(accNum, accCustType):
    performType = "transfer"
    while True:
        transferAccDest = input("Enter The Account Number To Be Transferred: ")
        file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
        count2 = -1
        success = False
        for rec in file:
            acc2 = rec.split(":")
            count2 += 1
            if (transferAccDest == acc2[1]):
                success = True
                accBalanceDest = float(acc2[9])
                break
        if success == True:
            break
        else: 
            print("INVALID Account Number!")
    
    while True: 
        transferAmount = float(input("Enter The Transfer Amount\n"
                            "RM: "))
        rmtransferAmount = "RM" + str(transferAmount)
        choice = input("\nConfirm Transfer " + rmtransferAmount + " From Your Bank Account To " + transferAccDest +"? [Yes/No]\n")
        if choice == "Yes":
            file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
            count1 = -1
            for rec in file:
                acc = rec.split(":")
                count1 += 1
                if (accNum == acc[1]):
                    accBalance = float(acc[9])
                    break

            if accCustType == "SAVINGS":
                minBal = float(100)
                transferRequirement(transferAccDest, accBalance, accBalanceDest, transferAmount, accNum, minBal, count1, count2, acc, acc2, performType)
                break
            elif accCustType == "CURRENT":
                minBal = float(500)
                transferRequirement(transferAccDest, accBalance, accBalanceDest, transferAmount, accNum, minBal, count1, count2, acc, acc2, performType)
                break

        elif choice == "No":
            while True:
                choice2 = input("Do You Wish To Continue Again? [Yes/No]\n")
                if choice2 == "Yes":
                    print("\nBe Sure To Enter The Right Amount!")
                    break
                elif choice2 == "No":
                    customerMenu(accNum)
                else:
                    print("INVALID INPUT!")
        
        else:
            print("INVALID INPUT!")

    return(accNum)
#--------------------------------------------------------------------------------------------------------------------------------
# CUSTOMER MODIFY PASSWORD PAGE

def modifyCustPass(accNum):
    while True:
        file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
        oldPass = input("\nEnter Your Current Password: \n")
        count = -1
        for rec in file:
            acc = rec.split(":")
            count += 1
            if accNum == acc[1]:
                accPass = acc[2]
                break

        if oldPass == accPass:
            while True:
                newPass = input("\nEnter Your New Password: \n")
                newPassConfirmed = input("\nConfirm Your New Password: \n")

                if newPassConfirmed == newPass:
                    file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
                    newRec = file.readlines()
                    
                    newRec[count] = f"{acc[0]}:{acc[1]}:{newPass}:{acc[3]}:{acc[4]}:{acc[5]}:{acc[6]}:{acc[7]}:{acc[8]}:{acc[9]}"

                    file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","w")
                    file.writelines(newRec)
                    file.close()

                    print("\nPassword Successfully Changed!\n")
                    break
            
                elif newPassConfirmed != newPass:
                    print("Password Do Not Match! ... Please Try Again.\n")

            return(accNum)

        elif oldPass != accPass:
            print("Wrong Password! ... Please Try Again.\n")

#--------------------------------------------------------------------------------------------------------------------------------
# CUSTOMER BALANCE PAGE

def accBalance(accNum):
    file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
    count = -1
    for rec in file:
        acc = rec.split(":")
        count += 1
        if (accNum == acc[1]):
            accBalance = float(acc[9])
            break
    
    print("\nYour Current Balance: " + "RM" + str(accBalance) + "\n")

    return(accNum)
    
#--------------------------------------------------------------------------------------------------------------------------------
# CUSTOMER WITHDRAWAL REQUIREMENT PAGE

def withdrawRequirement(accBalance, withdrawAmount, accNum, minBal, count, acc, performType):
    if accBalance <= minBal:
        print("\nWithdrawal Request DENIED.")
        print("PS: Current Balance Under Minimum Requirement (RM" + str(minBal) + ") !\n"
                "Current Balance: " + str(accBalance) + "\n"
                "\nBack to Home Page")
        customerMenu(accNum)

    elif accBalance > minBal:
        notRoundedAvalBal = accBalance - minBal
        availableBalance = round(notRoundedAvalBal, 2)
        if withdrawAmount > availableBalance:
            print("\nWithdrawal Request DENIED.\n"
                "Withdrawal Amount Exceeds Minimum Balance (RM" + str(minBal) + ") ! ... Please Try Again.\n"
                "\nCurrent Available Balance For Withdrawal: RM" + str(availableBalance) + "\n")

        elif withdrawAmount <= availableBalance:
            notRoundedBal = accBalance - withdrawAmount
            newAccBalance = round(notRoundedBal, 2)

            file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
            newRec = file.readlines()
            
            newRec[count] = f"{acc[0]}:{acc[1]}:{acc[2]}:{acc[3]}:{acc[4]}:{acc[5]}:{acc[6]}:{acc[7]}:{acc[8]}:{newAccBalance}\n"

            file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","w")
            file.writelines(newRec)
            file.close()
            
            print("\nWithdrawal Success!\n"
                "Your Current Balance: ", "RM" + str(newAccBalance) + "\n")
            none = None
            none1 = None 
            none2 = None
            statementAccReport(accBalance, withdrawAmount, accNum, performType, newAccBalance, none, none1, none2)
            
            return(accNum)

#--------------------------------------------------------------------------------------------------------------------------------
# WITHDRAWAL PAGE
def custWithdrawal(accNum, accCustType):
    performType = "withdrawal"
    while True:
        withdrawAmount = float(input("Enter The Withdrawal Amount\n"
                            "RM: "))
        rmwithdrawAmount = "RM" + str(withdrawAmount)
        choice = input("\nConfirm Withdraw " + rmwithdrawAmount + " From Your Bank Account? [Yes/No]\n")
        if choice == "Yes":
            file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
            count = -1
            for rec in file:
                acc = rec.split(":")
                count += 1
                if (accNum == acc[1]):
                    accBalance = float(acc[9])
                    break

            if accCustType == "SAVINGS":
                minBal = float(100)
                withdrawRequirement(accBalance, withdrawAmount, accNum, minBal, count, acc, performType)
                break
            
            elif accCustType == "CURRENT":
                minBal = float(500)
                withdrawRequirement(accBalance, withdrawAmount, accNum, minBal, count, acc, performType)
                break
        
        elif choice == "No":
            while True:
                choice2 = input("Do You Wish To Continue Again? [Yes/No]\n")
                if choice2 == "Yes":
                    print("\nBe Sure To Enter The Right Amount!")
                    break
                elif choice2 == "No":
                    customerMenu(accNum)
                else:
                    print("INVALID INPUT!")
        
        else:
            print("INVALID INPUT!")

    return(accNum)
#--------------------------------------------------------------------------------------------------------------------------------
# DEPOSIT PAGE

def custDeposit(accNum):
    performType = "deposit"
    while True:
        depoAmount = float(input("Please Enter The Amount To Be Deposited\n"
                            "RM: "))
        rmDepoAmount = "RM" + str(depoAmount)
        choice = input("\nConfirm Deposit " + rmDepoAmount + " To Your Bank Account? [Yes/No]\n")
        if choice == "Yes":
            file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
            count = -1
            for rec in file:
                acc = rec.split(":")
                count += 1
                if (accNum == acc[1]):
                    accBalance = float(acc[9])
                    break

            notRoundedBal = accBalance + depoAmount                    
            newAccBalance = round(notRoundedBal, 2)
            
            file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
            newRec = file.readlines()
            
            newRec[count] = f"{acc[0]}:{acc[1]}:{acc[2]}:{acc[3]}:{acc[4]}:{acc[5]}:{acc[6]}:{acc[7]}:{acc[8]}:{newAccBalance}\n"

            file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","w")
            file.writelines(newRec)
            file.close()

            print("\nDeposit Success!"
                "\nYour Current Balance: ", "RM" + str(newAccBalance) + "\n")
            none = None
            none1 = None
            none2 = None
            statementAccReport(accBalance, depoAmount, accNum, performType, newAccBalance, none, none1, none2)
            break

        elif choice == "No":
            while True:
                choice2 = input("Do You Wish To Continue Again? [Yes/No]\n")
                if choice2 == "Yes":
                    print("\nBe Sure To Enter The Right Amount!")
                    break
                elif choice2 == "No":
                    customerMenu(accNum)
                else:
                    print("INVALID INPUT!")
        
        else:
            print("INVALID INPUT!\n")

    return(accNum)
#--------------------------------------------------------------------------------------------------------------------------------
# MODIFY CUSTOMER DETAILS

def modifyCustomerData(acc, count, accName):
    while True:
        file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
        newData = acc
        option = int(input("\nPlease Enter The Option Below For Data To Be Edited: \n"
                        "\n1. Phone Number"
                        "\n2. Email"
                        "\n3. Place of Birth"
                        "\n4. Date of Birth"
                        "\n5. Customer Account Type [SAVINGS/CURRENT]\n"
                        "\nChoose A Number[1/2/3/4/5]: "))
        updatedData = input("Enter The New Changes: ")
        newRec = file.readlines()
        if option == 1:  
            newRec[count] = f"{newData[0]}:{newData[1]}:{newData[2]}:{newData[3]}:{updatedData}:{newData[5]}:{newData[6]}:{newData[7]}:{newData[8]}:{newData[9]}"
            break
        elif option == 2:
            newRec[count] = f"{newData[0]}:{newData[1]}:{newData[2]}:{newData[3]}:{newData[4]}:{updatedData}:{newData[6]}:{newData[7]}:{newData[8]}:{newData[9]}"
            break
        elif option == 3:
            newRec[count] = f"{newData[0]}:{newData[1]}:{newData[2]}:{newData[3]}:{newData[4]}:{newData[5]}:{updatedData}:{newData[7]}:{newData[8]}:{newData[9]}"
            break
        elif option == 4:
            newRec[count] = f"{newData[0]}:{newData[1]}:{newData[2]}:{newData[3]}:{newData[4]}:{newData[5]}:{newData[6]}:{updatedData}:{newData[8]}:{newData[9]}"
            break
        elif option == 5:
            newRec[count] = f"{newData[0]}:{newData[1]}:{newData[2]}:{newData[3]}:{newData[4]}:{newData[5]}:{newData[6]}:{newData[7]}:{updatedData}:{newData[9]}"
            break
        else: 
            while (option > 5 or option < 1):
                print("Invalid number!")
                option = int(input("Enter an option based on the number: "))

    file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","w")
    file.writelines(newRec)
    file.close()

    file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
    wholeList = file.readlines()
    accRec = wholeList[count]
    newAccData = accRec.split(":")

    print("\nAccount Successfully Updated!\n")
    print("Current Customer's Profile Details\n" 
          "------------------------------------\n"
          "\nName: " + newAccData[3] + "\n"
          "Phone Number: " + newAccData[4] + "\n"
          "E-mail: " + newAccData[5] + "\n"
          "Place of Birth: " + newAccData[6] + "\n"
          "Date of Birth: " + newAccData[7] + "\n"
          "Account Type: " + newAccData[8] + "\n"
          "Balance: "+ newAccData[9])
    
    while True:
        choice = input("Do You Wish To Continue Modifying The Current Account? [Yes/No]\n")
        if choice == "Yes":
            modifyCustomerData(acc, count, accName)
        elif choice == "No":
            adminMenu(accName)
        else:
            print("INVALID Input!")

#--------------------------------------------------------------------------------------------------------------------------------
# REGISTER ADMIN PERSONAL DATA

def regAdminDetails(uniqueId):
    print("\nCREATE A NEW ADMIN ACCOUNT")
    print("--------------------------------------------------------------")
    print("\nPlease enter the following new Admin's details to register.\n")

    name = input("Admin's name: ")
    phoneNum = input("Admin's phone number: ")
    email = input("Admin's email: ")
    placeOfBirth = input("Admin's place of birth [City, Country]: ")
    birthDate = input("Admin's date of birth [dd/mm/yyyy]: ")

    file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","a")
    file.write(name + ":" + phoneNum + ":" + email + ":" + placeOfBirth + ":" + birthDate + "\n")
    file.close()

    newUsername = "AMDN"+ str(uniqueId)
    newPassword = "admin101"

    print("\nAccount Successfully Registered!\n")
    print("Username = " + newUsername + "\n")
    print("Password = " + newPassword + "\n")

    choice = input("Do you wish to continue? [Yes/No]\n")
    if choice == "Yes":
        superUserMenu()
    else:
        loginMenuId()

#--------------------------------------------------------------------------------------------------------------------------------
# REGISTER CUSTOMER PERSONAL DATA

def regCustDetails(uniqueId,custAccTypeData,accName):
    print("                \nCREATE A NEW CUSTOMER ACCOUNT\n")
    print("--------------------------------------------------------------")
    print("\nPlease enter the following new Customer's details to register.\n")

    name = input("Customer's name: ")
    phoneNum = input("Customer's phone number: ")
    email = input("Customer's email: ")
    placeOfBirth = input("Customer's place of birth [City, Country]: ")
    birthDate = input("Customer's date of birth [dd/mm/yyyy]: ")
    if custAccTypeData == "SAVINGS":
        balance = float(100)
    elif custAccTypeData == "CURRENT":
        balance = float(500)

    file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","a")
    file.write(name + ":" + phoneNum + ":" + email + ":" + placeOfBirth + ":" + birthDate + ":" + custAccTypeData + ":" + str(balance) + "\n")
    file.close()

    print("\nAccount Successfully Registered!\n")
    print("Username = CUST" + str(uniqueId) + "\n")
    print("Password = user1234\n")
    
    while True:
        choice = input("Do you wish to continue? [Yes/No]\n")
        if choice == "Yes": 
            adminMenu(accName)
        elif choice == "No":
            loginMenuId()
        else:
            print("INVALID INPUT!")

#--------------------------------------------------------------------------------------------------------------------------------
# CUSTOMER MENU

def customerMenu(accNum):
    file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
    for rec in file:
        acc = rec.split(":")
        if accNum == acc[1]:
            accCustType = acc[8]
            accName = acc[3]     
            
    print("\nGood Morning/Afternoon/Evening Customer [" + accName + "], Please Select An Option Below: \n"
          "-----------------------------------------------------------------------------------\n")
    print("1 = Deposit")
    print("2 = Withdrawal")
    print("3 = Transfer")
    print("4 = Balance")
    print("5 = Modify Password")
    print("6 = Statement of Account Report")
    print("7 = Exit")
    option = input("\nSelect A Number: ")
    while True:
        if option == "1":
            custDeposit(accNum)
            break
        elif option == "2":
            custWithdrawal(accNum, accCustType)
            break
        elif option == "3":
            custTransfer(accNum, accCustType)
            break    
        elif option == "4":
            accBalance(accNum)
            break
        elif option == "5":
            modifyCustPass(accNum)
            break
        elif option == "6":
            generateReport(accNum)
            break
        elif option == "7":
            print("Thank You For Choosing CENTRAL BANK :) ... Have A Nice Day!")
            loginMenuId()
        else:
            print("INVALID Input!")
            option = input("\nEnter The Correct Number: ")
    
    while True:
        choice2 = input("\nDo You Wish To Continue? [Yes/No]\n")
        if choice2 == "Yes":
            customerMenu(accNum)
        elif choice2 == "No":
            print("Thank You For Choosing CENTRAL BANK :) ... Have A Nice Day!")
            loginMenuId()
        else:
            print("INVALID INPUT!")

#--------------------------------------------------------------------------------------------------------------------------------
# ADMIN MENU

def adminMenu(accName):
    print("         Good Morning/Afternoon/Evening Admin [" + accName +"]\n"
          "--------------------------------------------------------------")
    print("\nPlease Select An Option Below:\n "
            "\n1. Create New Customer Account"
            "\n2. Modify Customer Details"
            "\n3. Customer Statement of Account Report"
            "\n4. Exit")
    option = int(input("\nEnter an option based on the number: \n"))
    
    while option >= 0:
        if option == 1:
            file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
            for rec in file:
                acc = rec.split(":")
                accNum = acc[1]
                uniqueId = int(accNum[4:8])
                uniqueId += 1
            file.close()

            file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","a")
            file.write("C" + ":" + "CUST" + str(uniqueId) + ":" + "user1234" + ":")
            file.close()

            print("Select Customer's Type Of Account: \n")
            while True:
                custAccType = input("\nS = Savings Account [Minimum Balancel: RM100]"
                                    "\nC = Current Account [Minimum Balance: RM500]\n"
                                    "\nEnter a letter [S/C]: \n")
                
                if custAccType == "S":
                    custAccTypeData = "SAVINGS"
                    break
                elif custAccType == "C":
                    custAccTypeData = "CURRENT"
                    break
                else:
                    print("INVALID Input!")
                
            regCustDetails(uniqueId,custAccTypeData,accName)

        elif option == 2:
            while True:
                file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
                accNum = input("\nEnter Customer's Bank Account Username: \n")
                flag = 0
                count = -1
                for rec in file:
                    acc = rec.split(":")
                    count += 1
                    if accNum == acc[1]:                       
                        flag = 1
                        break                      
                file.close()

                if flag == 1:
                    modifyCustomerData(acc, count, accName)
                else:
                    print("\nINVALID Username ... Please Try Again.")
               
        elif option == 3:
            while True:
                file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
                accNum = input("\nEnter Customer's Bank Account Username: \n")
                flag = 0
                count = -1
                for rec in file:
                    acc = rec.split(":")
                    count += 1
                    if accNum == acc[1]:                       
                        flag = 1
                        break                      
                file.close()

                if flag == 1:
                    generateReport(accNum)
                    break
                else:
                    print("\nINVALID Username ... Please Try Again.")
            
            while True:
                choice2 = input("\nDo You Wish To Continue Again? [Yes/No]\n")
                if choice2 == "Yes":
                    break
                elif choice2 == "No":
                    adminMenu(accName)
                    break
                else:
                    print("INVALID INPUT!")

        elif option == 4:
            loginMenuId()
            break
        else:
            while (option > 4 or option < 1):
                print("Invalid number!")
                option = int(input("Enter an option based on the number: "))
    
#--------------------------------------------------------------------------------------------------------------------------------
# SUPER USER MENU

def superUserMenu():
    print("Good Morning/Afternoon/Evening SuperUser\n")
    while True:
        choice = input("Proceed to create a new Admin Account? [Yes/No] \n")
        if choice == "Yes":
            file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
            for rec in file:
                acc = rec.split(":")
                accNum = acc[1]
                uniqueId = int(accNum[4:8])
                uniqueId += 1
            file.close()
            break    
        elif choice == "No":
            loginMenuId()
        else:
            print("INVALID Input!")
    
    file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","a")
    file.write("A" + ":" + "ADMN" + str(uniqueId) + ":" + "admin101" + ":" )
    file.close()

    regAdminDetails(uniqueId)
    
#--------------------------------------------------------------------------------------------------------------------------------
# LOGIN PAGE

def loginMenuPass(accPass, accType, accNum, accName):
    while True:
        file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
        password = input("\nEnter Your Account Password: ")      
        success = False 
        if (password == accPass):
            success = True
        file.close()

        if success == True:
            print("\nLogin Successful!!!\n")
            if accType == "S":
                superUserMenu()
                break
            elif accType == "A":
                adminMenu(accName)
                break
            elif accType == "C":
                customerMenu(accNum)
        else:
            print("\nInvalid Password ... Please try again.\n")

def loginMenuId():
    print("\n<<<<<<<<<<<<<<<<<<<  WELCOME TO CENTRAL BANK  >>>>>>>>>>>>>>>>>\n")
    print("\n                           LOGIN MENU\n"
        "--------------------------------------------------------------")
    while True:
        file = open("C:\\Users\\ASUS\\OneDrive\\Desktop\\Apu CSDA\\Y1 Sem 1\\PYP\\FinalPYPSem1\\data.txt","r")
        accNum = input("\nEnter Your Account Username: ")
        success = False
        for rec in file:
            acc = rec.split(":")
            if (accNum == acc[1]):
                success = True
                accPass = acc[2]
                accType = acc[0]
                accName = acc[3]
                break
        file.close()

        if success == True:
            loginMenuPass(accPass, accType, accNum, accName)          
            break
        else:
            print("\nInvalid Username ... Please try again.")

#--------------------------------------------------------------------------------------------------------------------------------
 
loginMenuId()