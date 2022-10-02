import os

def B_sheet(b_name):
    pat = os.path.join(b_name , "Accounts")
    accs = os.listdir(pat)
    liab_accs = []
    asset_accs = []
    eq_accs = []
    t_asset = 0
    t_liab = 0
    t_eq = 0
    for i in accs:
        c_acc = os.path.join(pat , i)
        if os.path.isfile(c_acc) == False:
            accs.remove(i)
            continue
        with open(c_acc , "r") as f:
            info = f.read()
            info = info.strip().split(",")
            if info[0] == "asset":
                asset_accs.append(info)
            elif info[0] == "liab":
                liab_accs.append(info)
            elif info[0] == "eq":
                eq_accs.append(info)
    pat = os.path.join(b_name , "latest_date.txt")
    with open(pat , "r") as f:
        d = f.read().strip()
    d = d.split("/")
    d = "-".join(d)
    pat = os.path.join(b_name , "Balance Sheet" , d)
    pat += ".csv"
    rep = os.path.join(".")
    b = b_name[11:]
    with open(pat , "w") as f:
        f.write("-,-,-,-,-\n")
        f.write("-,-,-,-,-\n")
        f.write(" , ,Balance Sheet, , \n")
        f.write(" , ,")
        f.write(b)
        f.write(", , \n")
        f.write(" , ,")
        f.write(d)
        f.write(", , \n")
        f.write("Assets, , ,Liabilities & Equity , \n")
        while True:
            if len(asset_accs) != 0:
                for i in asset_accs:
                    f.write(i[1])
                    f.write(",")
                    f.write(i[2])
                    f.write(", ,")
                    t_asset += int(i[2])
                    asset_accs.remove(i)
                    break
            if len(liab_accs) != 0:
                for i in liab_accs:
                    f.write(i[1])
                    f.write(",")
                    f.write(i[2])
                    f.write("\n")
                    t_liab += int(i[2])
                    liab_accs.remove(i)
                    break
            else:
                f.write(" , \n")
            if len(asset_accs) == 0 and len(liab_accs) == 0:
                f.write("Total Assets,")
                f.write(str(t_asset))
                f.write(", ,Total Liabilities,")
                f.write(str(t_liab))
                f.write("\n")
                f.write(" , , ,Owner's Equity, \n")
                f.write(" , , ,")
                f.write(eq_accs[0][1])
                f.write(",")
                f.write(eq_accs[0][2])
                f.write("\n")
                f.write(" , , ,Total Liab + Eq,")
                f.write(str(t_liab + int(eq_accs[0][2])))
                f.write("\n-,-,-,-,-\n")
                f.write("-,-,-,-,-\n")
                break



