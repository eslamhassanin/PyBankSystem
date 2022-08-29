# -*- coding: utf-8 -*-
import sys
import re
import random

def admin_function():
    print("\nWelcome Admin")
    print("1. Display New Customer’s Registration Request.")
    print("2. Approve / Reject New Customer detail.")
    print("3. Provide Loan detail to New Registered Customer.")
    print("4. Search and Display all transactions of specific customer.")
    print("5. Search and Display all transactions of specific Loan type (EL/CL/HL/PL).")
    print("6. Display all transaction of all customer.")
    print("7. Display all transaction of all types of Loan.")
    print("8. Exit")
    optionAdmin=input("Kindly enter your choice: 1/2/3/4/5/6/7/8\n")
    if optionAdmin=='1':
        f = open("New_Customer.txt", "r")
        print(f.read())
        admin_function()
    elif optionAdmin=='2':
        f = open("New_Customer.txt", "r")
        print(f.read())
        cId=input("Enter Customer ID: ")
        file = open("New_Customer.txt", "r")
        data= file.readlines()
        DATA=[]
        for line in data:
            arr=line.split(' ')
            DATA.append(arr)
        customer=[]
        for i in range(len(DATA)):
            if DATA[i][0]==cId:
                customer=DATA[i]
        for i in customer:
            print(i,end = " ")
        status=input("Enter Status: ")
        customer[3]=customer[3][:-1]
        customer.append(status)
        print(customer)
        if(status=="approved" or status=="Approved"):
            f = open("Registered_Customer.txt","a")
            for i in customer:
                f.write(i)
                f.write(" ")
            f.write('\n')    
            f.close()
        elif(status=="rejected" or status=="Rejected"):
            f = open("Rejected_Customer.txt","a")
            for i in customer:
                f.write(i)
                f.write(" ")
            f.write('\n')    
            f.close()
        admin_function()    
    elif optionAdmin=='3':
        f = open("Registered_Customer.txt", "r")
        print(f.read())
        cId=input("Enter Customer ID: ")
        file = open("Registered_Customer.txt", "r")
        data= file.readlines()
        DATA=[]
        for line in data:
            arr=line.split(' ')
            DATA.append(arr)
        customer=[]
        for i in range(len(DATA)):
            if DATA[i][0]==cId:
                customer=DATA[i]
        for i in customer:
            print(i,end = " ")
        num = random.randint(0,10000)
        installmentdate=input("Enter installment date: ")
        installmonth=input("Enter installment per month: ")
        loanterm=input("Enter loan term: ")
        loantype=input("Enter loan type (EL/HL/PL/CL): ")
        loanstatus=input("Enter status: ") 
        f = open("Loan_Registered_Customer.txt","a")
        f.write(str(num)+' '+installmentdate+' '+installmonth+' '+loanterm+' '+loanstatus+' '+customer[0]+' '+customer[1]+' '+loantype)
        f.write('\n')    
        f.close()
        admin_function()
    elif optionAdmin=='4':
        option3=input("1. Customer ID\n2.Loan ID\n")
        if option3=='1':
            ID=input("Enter Customer ID: ")
            file = open("Loan_Registered_Customer.txt", "r")
            data= file.readlines()
            DATA=[]
            for line in data:
                 arr=line.split(' ')
                 DATA.append(arr)
            customer=[]
            for i in range(len(DATA)):
                 if DATA[i][5]==ID:
                     customer=DATA[i]
                     for i in customer:
                         print(i,end = " ")
                     if not customer:
                         print("Invalid Customer ID")
        if option3=='2':
            ID=input("Enter Loan ID: ")
            file = open("Loan_Registered_Customer.txt", "r")
            data= file.readlines()
            DATA=[]
            for line in data:
                 arr=line.split(' ')
                 DATA.append(arr)
            customer=[]
            for i in range(len(DATA)):
                 if DATA[i][1]==ID:
                     customer=DATA[i]
                     for i in customer:
                         print(i,end = " ")
                     if not customer:
                         print("Invalid Loan ID")
        admin_function()  
    elif optionAdmin=='5':
        TYPE=input("Enter Loan Type (EL/HL/PL/CL): ")
        if(TYPE!="EL" and TYPE!="HL" and TYPE!="PL" and TYPE!="CL"):
            print("Invalid Loan Type")
        else:            
            file = open("Loan_Registered_Customer.txt", "r")
            data= file.readlines()
            DATA=[]
            for line in data:
                arr=line.split(' ')
                DATA.append(arr)  
            customer=[]
            for i in range(len(DATA)):    
                DATA[i][6]=DATA[i][6][:-1]  
                if DATA[i][6]==TYPE:
                     customer=DATA[i]
                     for i in customer:
                         print(i,end = " ")
                     print('\n')
        admin_function()
    elif optionAdmin=='6':
        f = open("Customer_Transaction.txt", "r")
        print(f.read())
        admin_function()
    elif optionAdmin=='7':
        f = open("Customer_Transaction.txt", "r")
        print(f.read())
        admin_function()       
    else:
        sys.exit()

def approvedCustomer(userid):
    print("Welcome to Malaysia Bank")
    print("1. Check Loan detail as per filled at the time of registration with Loan Instalment Date and Loan ID generated by Admin.")
    print("2. Can pay Loan Instalment.")
    print("3. Can view the own transactions.")
    print("4. Can check the status of Loan.")
    print("5. Exit")
    customerOption=input("Kindly enter your choice: 1/2/3/4/5\n")
    if customerOption=='1':
        file = open("Loan_Registered_Customer.txt", "r")
        data= file.readlines()
        DATA=[]
        for line in data:
            arr=line.split(' ')
            DATA.append(arr)
        customer=[]
        for i in range(len(DATA)):
            if DATA[i][5]==userid:
                customer=DATA[i]
                customer[7]=customer[7][:-1]
                for i in customer:
                    print(i, end = " " )
        approvedCustomer(userid)
    elif customerOption=='2':
        file = open("Loan_Registered_Customer.txt", "r")
        data= file.readlines()
        DATA=[]
        for line in data:
            arr=line.split(' ')
            DATA.append(arr)
        customer=[]
        for i in range(len(DATA)):
            if DATA[i][5]==userid:
                customer=DATA[i]
                customer[7]=customer[7][:-1]
                print(customer[0]+' '+customer[1]+' '+customer[2]+' ')
        amount=input("Enter amount: ")
        date=input("Enter date: ")
        f = open("Customer_Transaction.txt","a")
        f.write(customer[5]+' ')
        f.write(customer[0]+' ')
        f.write(amount+' ')
        f.write(date+' ')
        if date==customer[1]:
            f.write("Installement Paid ")
        else:
            f.write("Installement Overdue ")
        f.write('\n')    
        f.close()
        approvedCustomer(userid)
    elif customerOption=='3':
        file = open("Customer_Transaction.txt", "r")
        data= file.readlines()
        DATA=[]
        for line in data:
            arr=line.split(' ')
            DATA.append(arr)
        customer=[]
        for i in range(len(DATA)):
            if DATA[i][0]==userid:
                customer=DATA[i]
                customer[4]=customer[4][:-1]
                for i in customer:
                    print(i, end = " " )
                print('\n')    
        approvedCustomer(userid)
    elif customerOption=='4':
        file = open("Customer_Transaction.txt", "r")
        data= file.readlines()
        DATA=[]
        for line in data:
            arr=line.split(' ')
            DATA.append(arr)
        customer=[]
        for i in range(len(DATA)):
            if DATA[i][0]==userid:
                customer=DATA[i]
                customer[4]=customer[4][:-1]
                for i in customer:
                    print(i, end = " " )
                print('\n')    
        approvedCustomer(userid)
    else:
        sys.exit()

def validateUser():
    userid=input("User ID: ")
    file = open("Login_Customer.txt", "r")
    data= file.readlines()
    DATA=[]
    for line in data:
        arr=line.split(',')
        DATA.append(arr)
    customer=[]
    for i in range(len(DATA)):
        if DATA[i][0]==userid:
            customer=DATA[i]
            customer[1]=customer[1][:-1]
            pswd=input("Password: ")
            if pswd==customer[1]:
                file = open("Registered_Customer.txt", "r")
                data= file.readlines()
                DATA=[]
                for line in data:
                    arr=line.split(' ')
                    DATA.append(arr)
                boolean=False
                customer=[]
                for i in range(len(DATA)):
                    if DATA[i][0]==userid:
                        customer=DATA[i]
                        if (customer[4]=='Approved' or customer[4]=='approved'):
                            boolean=True
                if not boolean:
                    print("Account approval pending")
                    return 
                else:
                    approvedCustomer(userid)
                    return boolean
            else:
                print("Invalid credentials, Enter again.")
                return boolean
        if not customer:
            print("Invalid User ID ")
            return boolean    

def registeredCustomer():
    print("Welcome to Malaysia Bank")
    print("Kindly enter Login Details:")
    while True:
        flag= validateUser()
        if flag:
            break
        elif None:
            break
            

def newCustomer():
    print("Welcome to Malaysia Bank")  
    print("1. Check loan detail")
    print("2. Loan calculator for loan amount eligibility")
    print("3. Register with Malaysian Bank")
    print("4. Back to Customer Menu")
    print("5. Exit")
    customerOption=input("Kindly enter your choice: 1/2/3/4/5\n")
    if customerOption=='1':
        print("1. Education Loan (EL)")
        print("2. Car Loan (CL)")
        print("3.  Home Loan (HL)")
        print("4.  Personal Loan (PL)")
        print("5. Back to New Customer Menu")
        option1=input("Kindly enter your choice: 1/2/3/4\n")
        if option1=='1':
            f = open("Education_loan.txt", "r")
            print(f.read())
        elif option1=='2':
            f = open("Car_Loan.txt", "r")
            print(f.read())
        elif option1=='3':
            f = open("Home_Loan.txt", "r")
            print(f.read())
        elif option1=='4':
            f = open("Personal_Loan.txt", "r")
            print(f.read())
        else:
            newCustomer()
    elif customerOption=='2':
        amount=input("Enter Loan Amount: ")
        term=input("Enter Loan Term: ")
        installment=float(amount)/float(term)
        rate=(float(amount)*float(term)*12)/100
        print("Installment amount: "+str(installment))
        print("Interest Rate: "+str(rate)+'\n')
        newCustomer()
    elif customerOption=='3':
        userid=input("Enter User ID: ")
        pswd=input("Enter Password: ")
        email=input("Enter Email ID: ")
        dob=input("Enter Date of Birth: ")
        f = open("New_Customer.txt","a")
        f.write(userid+' '+pswd+' '+email+' '+dob+'\n')
        f.close()
        newCustomer()
    elif customerOption=='4':
        customer_function()
    else:
        sys.exit()
        
    

def customer_function():
    print("\nWELCOME TO MBOLMS")
    print("1. Login (if you are registered customer)")
    print("2. Sign up (if you are new customer)")
    print("3. Back to Main Menu")
    print("4. Exit")
    optionCustomer=input("Kindly enter your choice: 1/2/3/4\n")
    if optionCustomer=='1':
        registeredCustomer()
    elif optionCustomer=='2':
        newCustomer()
    elif optionCustomer=='3':
        main()
    else:
        sys.exit()


def main():
    print("WELCOME TO Malaysia Bank")
    print("User Types")
    print("1. Admin\n2. Customer\n3. Exit")
    option1=input("Kindly select your User Type: 1/2/3\n")
    
    if option1=='1':
        print("Welcome Admin")
        while True:
            print("Kindly enter Login Details:")
            userid=input("User ID:")
            pswd=input("Password:")
            if (userid=="admin" and pswd=="1234"):
                admin_function()
                break
            else:
                print("Invalid Credentials, Please enter again.")
    elif option1=='2':
        customer_function()
    else:
        sys.exit()
    
main()
