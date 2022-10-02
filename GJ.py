import csv
import os
from get_date import get_date

def credit(b_name , account , amount , date):
    ac_pat = os.path.join(b_name , "Accounts" , account)
    ac_pat += ".csv"
    led_pat = os.path.join(b_name , "Ledgers" , account)
    led_pat += ".csv"
    with open(ac_pat , "r") as f:
        i = f.read()
        i = i.strip().split(',')
        ac_type = i[0]
        c_amount = int(i[2])
    with open(ac_pat , "w") as f:
        if (ac_type) == "asset" or (ac_type) == "exp":
            f.write(ac_type)
            f.write(",")
            f.write(account)
            f.write(",")
            f.write(str(c_amount - amount))
        elif (ac_type) == "liab" or (ac_type) == "eq" or (ac_type) == "rev":
            f.write(ac_type)
            f.write(",")
            f.write(account)
            f.write(",")
            f.write(str(c_amount + amount))
    with open(led_pat , "a") as f:
        f.write("\n")
        f.write(date)
        f.write(", ,")
        f.write(str(amount))
        
def debit(b_name , account , amount , date):
    ac_pat = os.path.join(b_name , "Accounts" , account)
    ac_pat += ".csv"
    led_pat = os.path.join(b_name , "Ledgers" , account)
    led_pat += ".csv"
    with open(ac_pat , "r") as f:
        i = f.read()
        i = i.strip().split(',')
        ac_type = i[0]
        c_amount = int(i[2])
    with open(ac_pat , "w") as f:
        if (ac_type) == "asset" or (ac_type) == "exp":
            f.write(ac_type)
            f.write(",")
            f.write(account)
            f.write(",")
            f.write(str(c_amount + amount))
        elif (ac_type) == "liab" or (ac_type) == "eq" or (ac_type) == "rev":
            f.write(ac_type)
            f.write(",")
            f.write(account)
            f.write(",")
            f.write(str(c_amount - amount))
    with open(led_pat , "a") as f:
        f.write("\n")
        f.write(date)
        f.write(",")
        f.write(str(amount))
        f.write(", ")
        
def trial_balance(b_name):
    pat = os.path.join(b_name , "latest_date.txt")
    with open(pat , "r") as f:
        d = f.read()
        d = d.strip()
        d = "1/1/2020"
        d = d.split("/")
        d = "_".join(d)
    pat = os.path.join(b_name , "Accounts")
    accs = os.listdir(pat)
    asset_accs = []
    liab_accs = []
    eq_acc = []
    exp_accs = []
    rev_acc = []
    for i in accs:
        c_acc = os.path.join(pat , i)
        if os.path.isfile(c_acc) == False:
            accs.remove(i)
            continue
        with open(c_acc , "r") as f:
            info = f.read()
            info = info.strip().split(",")
            if (info[0]) == "asset":
                asset_accs.append(info)
            elif (info[0]) == "eq" :
                eq_acc.append(info)
            elif (info[0]) == "exp" :
                exp_accs.append(info)
            elif (info[0]) == "rev" :
                rev_acc.append(info)
            else:
                liab_accs.append(info)
    pat = os.path.join(b_name , "Trial Balance" , d)
    pat += ".csv"
    deb_side_sum = 0
    crd_side_sum = 0
    with open(pat , "w") as f:
        f.write("Account,Debit,Credit\n")
        for i in asset_accs:
            for j in i[1:]:
                f.write(j)
                f.write(",")
            deb_side_sum += int(j)
            f.write("\n")
        for i in exp_accs:
            for j in i[1:]:
                f.write(j)
                f.write(",")
            deb_side_sum += int(j)
            f.write("\n")
        for i in liab_accs:
            f.write(i[1])
            f.write(",,")
            f.write(i[2])
            f.write("\n")
            crd_side_sum += int(i[2])
        f.write(eq_acc[0][1])
        f.write(",,")
        f.write(eq_acc[0][2])
        f.write("\n")
        f.write(rev_acc[0][1])
        f.write(",,")
        f.write(rev_acc[0][2])
        f.write("\n")
        crd_side_sum += int(eq_acc[0][2])
        crd_side_sum += int(rev_acc[0][2])
        f.write(",")
        f.write(str(deb_side_sum))
        f.write(",")
        f.write(str(crd_side_sum))


def General_Journal(b_name):
    pat = os.path.join(b_name , "Accounts")
    accs = os.listdir(pat)
    for i in accs:
        if os.path.isfile(os.path.join(pat , i)) == False:
            accs.remove(i)
    ac_names = []
    for i in range(len(accs)):
        a_pat = os.path.join(pat , accs[i])
        with open(a_pat, "r") as f:
            data = csv.reader(f)
            for row in data:
                ac_names.append(row[1])
    op_accs = []
    crd_acc = []
    crd_am = []
    deb_acc = []
    deb_am = []
    while True:
        print("Already Selected Accounts: ")
        for i in op_accs:
            print(ac_names[i])
        print("\n\nPress: ")
        print("0 To Exit")
        for i in range(len(ac_names)):
            print(i+1 ,"For", ac_names[i])
        print(len(accs)+1,"To Proceed")
        try:
            des = int(input("Choose: "))
            if des == 0:
                return
            if (des > len(accs) + 1) or (des < 0):
                raise Exception
            if des == (len(accs) + 1):
                if (len(op_accs) >= 2):
                    break
                else:
                    print("Please Enter AtLeast Two Accounts")
                    continue
            des -= 1
            if des not in op_accs:
                op_accs.append(des)
            else:
                print("Account Already Selected!")
        except:
            print("Invalid Input!")
    while True:
        print("Which Account(s) you want to Debit")
        print("Press")
        print("0. To Exit")
        for i in range(len(op_accs)):
            print(i + 1 ,"For" , ac_names[op_accs[i]])
        print(len(op_accs) + 1 , "To Proceed")
        try:
            des = int(input("Enter: "))
            if des == 0:
                return
            if (des > len(op_accs) + 1) or des < 0:
                raise Exception
            if (des == len(op_accs) + 1):
                if(len(deb_acc) == 0):
                    print("Enter Atleast 1 account to Debit")
                    continue
                else:
                    break
            if(ac_names[op_accs[des - 1]]) not in deb_acc:
                deb_acc.append(ac_names[op_accs[des - 1]])
            if(len(deb_acc) == len(op_accs)):
                print("Invalid Entries have been made. Please Enter Again!")
                return
        except:
            print("Invalid Input")
    for i in op_accs:
        if (ac_names[i]) not in deb_acc:
            crd_acc.append(ac_names[i])
    print("Please Enter Amount(s) for the Account(s) Being Debited")
    for i in deb_acc:
        i += ": "
        while True:
            try:
                amm = int(input(i))
                deb_am.append(amm)
                break
            except:
                print("Invalid Input")

    print("Please Enter Amount(s) for the Account(s) Being Credited")
    for i in crd_acc:
        i += ": "
        while True:
            try:
                amm = int(input(i))
                crd_am.append(amm)
                break
            except:
                print("Invalid Input")
                        
    t_deb_am = 0
    for i in deb_am:
        t_deb_am += i
        
    t_crd_am = 0
    for i in crd_am:
        t_crd_am += i
        
    if(t_deb_am != t_crd_am):
        print("Invalid Entries have been made. Please Enter Again!")
        return
    
    print("Enter Date of Transacion: ")
    d = get_date(b_name)
    
    disc = input("Enter Discription: ")

    for i in range(len(deb_acc)):
        pat = os.path.join(b_name , "General Journal" , "GJ.csv")
        with open(pat , "a") as f:
            f.write("\n")
            if(i == 0):
                f.write(d)
            f.write(",")
            f.write(deb_acc[i])
            f.write(",")
            f.write(str(deb_am[i]))
            f.write(",")
            f.write("0")
            f.write(", ")
        debit(b_name , deb_acc[i] , deb_am[i] , d)

    for i in range(len(crd_acc)):
        pat = os.path.join(b_name , "General Journal" , "GJ.csv")
        with open(pat , "a") as f:
            f.write("\n")
            f.write(" ,")
            f.write(crd_acc[i])
            f.write(",")
            f.write("0")
            f.write(",")
            f.write(str(crd_am[i]))
            f.write(",")
            if(i == len(crd_acc) - 1):
                f.write(disc)
        credit(b_name , crd_acc[i] , crd_am[i] , d)
    trial_balance(b_name)
    
def end_acc_cycle(b_name):
    d = get_date(b_name)
    pat = os.path.join(b_name , "Accounts")
    accs = os.listdir(pat)
    req_accs = []
    for i in accs:
        c_acc = os.path.join(pat , i)
        if os.path.isfile(c_acc) == False:
            accs.remove(i)
            continue
        with open(c_acc , "r") as f:
            info = f.read()
            info = info.strip().split(",")
            if info[0] == "rev" or info[0] == "exp" or info[1] == "Drawing":
                req_accs.append(info)
    t_exp = 0
    for i in req_accs:
        i[2] = int(i[2])
        if (i[0] == "exp"):
            t_exp += i[2]
            credit(b_name , i[1] , i[2] , d)
            pat = os.path.join(b_name , "Accounts" , i[1])
            pat += ".csv"
            os.remove(pat)
            pat = os.path.join(b_name , "Ledgers" , i[1])
            pat += ".csv"
            os.remove(pat)
            req_accs.remove(i)
    for i in req_accs:
        if (i[0] == "rev"):
            debit(b_name , i[1] , i[2] , d)
            net_income = i[2] - t_exp
            req_accs.remove(i)
    if (net_income != 0):
        if(net_income > 0):
            credit(b_name , "Equity" , net_income , d)
        else:
            debit(b_name , "Equity" , abs(net_income) , d)
    if (req_accs[0][2] != 0):
        credit(b_name , req_accs[0][1] , int(req_accs[0][2]) , d)
        debit(b_name , "Equity" , int(req_accs[0][2]) , d)
    




    
    
    



