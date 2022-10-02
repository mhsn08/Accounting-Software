import pandas
import os
import pandas as pd
def Display_GJ(b_name):
    gj=os.path.join(b_name,"General Journal","GJ.csv")
    df=pd.read_csv(gj)
    pd.options.display.max_columns = len(df.columns)
    print(df)

