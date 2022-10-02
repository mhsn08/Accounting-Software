import datetime
import os

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
                print("Here")
                return b.strftime("%d/%m/%Y")
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
