import os
import datetime	
from c_acc import createAccount
from c_acc import get_info_for_account
from GJ import credit
from GJ import debit
from GJ import General_Journal
from GJ import end_acc_cycle
import pandas
import pandas as pd
from disp_gj import Display_GJ
from disp_led import Display_Led
from b_s import B_sheet
from disp_BS import Display_BS
from i_s import I_statement
from disp_IS import Display_IS

def get_date(b_name):
    while True:
        a = input("Enter Date in Format YYYY-MM-DD: ")
        a = a.split('-')
        try:
            for i in range(len(a)):
                a[i] = int(a[i])
            b = datetime.date( a[0] , a[1] , a[2])
            l_date = os.path.join(b_name , "latest_date.txt")
            if(os.path.isfile(l_date)) == False:
                b = b.strftime("%d/%m/%Y")
                with open(l_date , "w") as f:
                    f.write(b)
                return b
            with open(l_date , "r") as f:
                ld = f.read()
                ld = ld.strip()
                ld = datetime.datetime.strptime(ld , "%d/%m/%Y")
                ld = ld.date()
            if(ld > b):
                raise Exception
            b = b.strftime("%d/%m/%Y")
            with open(l_date , "w") as f:
                f.write(b)
            return b
        except:
            print("Invalid Input!")

def createBuisness(b_name):
    while True:
        try:
            os.mkdir("Projects")
            break
        except:
            break
    Buisness = os.path.join("." , "Projects" , b_name)
    try:
        os.mkdir(Buisness)
    except:
        print("Buisness Already Exist")
        return
    D = ["Accounts" ,"General Journal" , "Ledgers" , "Balance Sheet" , "Income Statement" , "Trial Balance"]
    for i in D:
        Buisness = os.path.join("." , "Projects" , b_name , i)
        os.mkdir(Buisness)
    Buisness = os.path.join("." , "Projects" , b_name)
    createNeccFiles(Buisness)
    
        
def listBuisness():
    try:
        pat = os.path.join("." , "Projects")
        names = os.listdir(pat)
    except:
        print("No Buisness has been Recorded")
        return False
    for i in range(len(names)):
        print(i + 1 , names[i])
    return names
        
def createNeccFiles(loc):
    acc = ["Equity.csv" , "Revenue.csv" , "Cash.csv" , "Drawing.csv" , "Notes Payable.csv", "Accounts Payable.csv"]
    for i in acc:
        pat = os.path.join(loc , "Ledgers" , i)
        with open(pat , "w") as f:
            f.write("Date,Debit,Credit")
    pat = os.path.join(loc , "Accounts" , acc[0])
    with open(pat , "w") as f:
        f.write("eq,Equity,")
        f.write("0")
    pat = os.path.join(loc , "Accounts" , acc[1])
    with open(pat , "w") as f:
        f.write("rev,Revenue,")
        f.write("0")
    pat = os.path.join(loc , "Accounts" , acc[2])
    with open(pat , "w") as f:
        f.write("asset,Cash,")
        f.write("0")
    pat = os.path.join(loc , "Accounts" , acc[3])
    with open(pat , "w") as f:
        f.write("asset,Drawing,")
        f.write("0")
    pat = os.path.join(loc , "Accounts" , acc[4])
    with open(pat , "w") as f:
        f.write("liab,Notes Payable,")
        f.write("0")
    pat = os.path.join(loc , "Accounts" , acc[5])
    with open(pat , "w") as f:
        f.write("liab,Accounts Payable,")
        f.write("0")
    pat = os.path.join(loc , "General Journal" , "GJ.csv")
    with open(pat , "w") as f:
        f.write("Date,Accounts,Debit,Credit,Discription")
    d = get_date(loc)
    print(d)
    pat = os.path.join(loc , "prev_cycle.txt")
    with open(pat , "w") as f:
        f.write(d)

    
    
    
def openBuisness():
    a = listBuisness()
    if a == False:
        return
    while True:
        try:
            des = int(input("Enter Which Buisness You want to deal with: "))
            if(des < 1 or des > len(a)):
                raise Exception
            break
        except:
            print("Invalid Input!")
    selected = os.path.join("." , "Projects" , a[des - 1])
    B_Operations(selected)
    
def B_Operations(b_name):
    while True:
        print("Please Enter your desired Operations\n")
        print("0. To Exit")
        print("1. Record Entry")
        print("2. End Accounting Cycle")
        print("3. Show Ledgers")
        print("4. Show General Journal")
        print("5. Create New Account")
        print("6. Show Balance Sheet")
        print("7. Show Income Statement")
        while True:
            try:
                op = int(input("Enter: "))
                if op == 0:
                    return
                if (op > 7 or op < 0):
                    raise Exception
                break
            except:
                print("Invalid Input!")
        if op == 5:
            get_info_for_account(b_name)
        if op == 1:
            General_Journal(b_name)
        if op == 2:
            end_acc_cycle(b_name)
        if op == 4:
            Display_GJ(b_name)
        if op == 3:
            Display_Led(b_name)
        if op == 6:
            B_sheet(b_name)
            Display_BS(b_name)
        if op == 7:
            I_statement(b_name)
            Display_IS(b_name)
            
            

        	
            
    

