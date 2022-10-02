import os
import datetime

def I_statement(b_name):
    pat = os.path.join(b_name , "Accounts")
    accs = os.listdir(pat)
    op_exp_accs = []
    for i in accs:
        c_acc = os.path.join(pat , i)
        if os.path.isfile(c_acc) == False:
            accs.remove(i)
            continue
        with open(c_acc , "r") as f:
            info = f.read()
            info = info.strip().split(",")
            if info[1] == "Coast of sales":
                c_sales = info
                continue
            elif info[1] == "Intrest":
                i_exp = info
                continue
            elif info[1] == "Tax":
                tax = info
                continue
            elif info[0] == "exp":
                op_exp_accs.append(info)
            elif info[0] == "rev":
                revenue = info
    c_date = os.path.join(b_name , "latest_date.txt")
    prev_date = os.path.join(b_name , "prev_cycle.txt")
    with open(c_date , "r") as f:
        d_c = f.read().strip()
    d_c = d_c.split("/")
    d_c = "-".join(d_c)
    pat = os.path.join(b_name , "Income Statement" , d_c)
    pat += ".csv"
    d_c = d_c.split("-")
    with open(prev_date , "r") as f:
        d_p = f.read().strip()
    d_p = d_p.split("/")
    for i in range(3):
        d_c[i] = int(d_c[i])
    for i in range(3):
        d_p[i] = int(d_p[i])
    p_d = datetime.datetime(d_p[2] , d_p[1] , d_p[0])
    c_d = datetime.datetime(d_c[2] , d_c[1] , d_c[0])
    diff_date = str(round((c_d.year - p_d.year) * 12 + c_d.month - p_d.month + (c_d.day - p_d.day)/30 , 2))
    for i in range(3):
        d_c[i] = str(d_c[i])
    d_c = "-".join(d_c)
    t_c_sales = 0
    try:
        t_c_sales += int(c_sales[2])
        g_pr = str(int(rev[2]) - int(c_sales[2]))
    except:
        g_pr = revenue[2]
    t_c_sales = str(t_c_sales)
    op_pr = int(g_pr)
    for i in op_exp_accs:
        op_pr -= int(i[2])
    op_pr = str(op_pr)
    tax = "0"
    try:
        n_i = int(op_pr)
        n_i -= int(tax[2])
        tax = str(tax[2])
    except:
        pass
    i_exp = "0"
    try:
        n_i -= (int(i_exp[2]))
        i_exp = i_exp[2]
    except:
        pass
    n_i = str(n_i)
    b = b_name[11:]
    with open(pat , "w") as f:
        f.write("-,-,-,-\n")
        f.write("-,-,-,-\n")
        f.write(" ,Income Statement, , \n")
        f.write(" ,For Time Period")
        f.write(diff_date)
        f.write(" Months, , \n")
        f.write(" ,")
        f.write(d_c)
        f.write(", , \n")
        f.write("Revenue, , ,")
        f.write(revenue[2])
        f.write("\n")
        f.write("Coast of Sales, ,")
        f.write(t_c_sales)
        f.write(", \n")
        f.write("Gross Profit, , ,")
        f.write(g_pr)
        f.write("\n")
        f.write("Operating Expances, , , \n")
        for i in op_exp_accs:
            f.write(i[1])
            f.write(", ,")
            f.write(i[2])
            f.write(", \n")
        f.write("Operating Profit, , ,")
        f.write(op_pr)
        f.write("\n")
        f.write("Taxes, ,")
        f.write(tax)
        f.write(", \n")
        f.write("Intrest, ,")
        f.write(i_exp)
        f.write(", \n")
        if int(n_i) >= 0:
            f.write("Net Income, , ,")
        else:
            f.write("Net Loss, , ,")
        f.write(str(n_i))
        f.write("\n")
        f.write("-,-,-,-\n")
        f.write("-,-,-,-\n")
       
    d_c = d_c.split("-")
    d_c = "/".join(d_c)
    with open(prev_date , "w") as f:
        f.write(d_c)



