import os
from bFun import createBuisness
from bFun import listBuisness
from bFun import openBuisness
from bFun import B_Operations
from bFun import createNeccFiles
from c_acc import get_info_for_account
from c_acc import createAccount
from get_date import get_date
from GJ import credit
from GJ import debit
from GJ import General_Journal
from GJ import end_acc_cycle
import pandas
import pandas as pd
from disp_gj import Display_GJ


while True:
    print("Enter Your Desire Operation\n")
    print("0. Quit")
    print("1. Create Buisness")
    print("2. List Buisness")
    print("3. Perform Operation in Buisness\n")
    while True:
        try:
            op = int(input("Choose: "))
            if(op >3 or op < 0):
                raise error
            else:
                break
        except:
            print("Invalid Input")
    if(op == 0):
        break
    elif(op == 1):
        b_name = input("Enter Buisness Name: ")
        createBuisness(b_name)
    elif(op == 2):
        listBuisness()
    else:
        openBuisness()
