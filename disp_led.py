import pandas
import os
import pandas as pd
def Display_Led(b_name):
    pat=os.path.join(b_name,"Accounts")
    accs = os.listdir(pat)
    acc_names = []
    for i in accs:
        if os.path.isfile(os.path.join(pat , i)) == False:
            accs.remove(i)
            continue
        ac_pat = os.path.join(pat , i)
        with open(ac_pat , "r") as f:
            name = f.read().strip().split(",")
            name = name[1]
            acc_names.append(name)
    while True:
        print("Enter Which Account(s) ledger you want to see: ")
        for i in range(len(acc_names)):
            print(i + 1, "For" , acc_names[i])
        try:
            des = int(input("Enter: "))
            des -= 1
            if des < 0 or des >= len(acc_names):
                raise Exception
            break
        except:
            print("Invalid Input")
    pat=os.path.join(b_name,"Ledgers" , accs[des])
    df=pd.read_csv(pat)
    pd.options.display.max_columns = len(df.columns)
    print(df)
