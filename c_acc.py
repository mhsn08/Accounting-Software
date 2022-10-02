import os

def createAccount(b_name , account_title , account_type):
    account = os.path.join(b_name , "Accounts" , account_title)
    account += ".csv"
    if os.path.isfile(account):
        print("Account Already Exists!!")
        return
    led = os.path.join(b_name , "Ledgers" , account_title)
    led += ".csv"
    with open(account , "w") as f:
        if(account_type == 1):
            ac_det = "asset," + account_title + ",0"
            f.write(ac_det)
        elif(account_type == 2):
            ac_det = "liab," + account_title + ",0"
            f.write(ac_det)
        else:
            ac_det = "exp," + account_title + ",0"
            f.write(ac_det)
    with open(led , "w") as f:
        f.write("Date,Debit,Credit")

def get_info_for_account(b_name):
    print("Please Enter Account Type. Press:\n")
    while(1):
        print("0. To Exit")
        print("1. For Asset Account")
        print("2. For Liability Account")
        print("3. For Expance Account")
        account_type = input("Enter Account Type: ")
        try:
            account_type = int(account_type)
            if(account_type == 0):
                return
            if(account_type > 3 or account_type < 1):
                raise Exception
            break
        except:
            print("Invalid Input!")
    account_title = input("Enter Account Title: ")
    createAccount(b_name , account_title , account_type)
    



