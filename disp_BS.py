import pandas
import os
import pandas as pd
def Display_BS(b_name):
    pat = os.path.join(b_name , "latest_date.txt")
    with open(pat , "r") as f:
        d = f.read().strip()
    d = d.split("/")
    d = "-".join(d)
    pat = os.path.join(b_name , "Balance Sheet" , d)
    pat += ".csv"
    df=pd.read_csv(pat)
    pd.options.display.max_columns = len(df.columns)
    print(df)

