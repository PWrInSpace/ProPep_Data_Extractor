import csv

file = open("data.txt", "r")

lines = file.readlines()


Run = 1
M = []
dataFlag = False
Isp = []
T = []
k = []
cstar = []

for line in lines:
    if "Run" in line:
        Run = ""
        for char in line:
            if char.isnumeric():
                Run = Run+char
            if char == "o":
                break
        Run = int(Run)
        
        M.append("")
        Isp.append("")
        T.append("")
        k.append("")
        cstar.append("")
        print("Run: ", Run)

    if ("THE MOLECULAR WEIGHT OF THE MIXTURE IS" in line and M[Run-1] == ""):
        for char in line:
            if char.isnumeric() or char == ",":
                if char == ",":
                      char = "."
                M[Run-1] = M[Run-1]+char
        M[Run-1] = float(M[Run-1])
        print("Molecular weight: ", M[Run-1], " g/mol")
    if ("IMPULSE" in line):
        dataFlag = True
        continue

    if dataFlag == True:
        i = 0 # 0 - ISP, 1 - k, 2 - T*, 4 - c*
        nextFlag = False
        for char in line:
            if char.isnumeric() or char == ",":
                nextFlag = True
                if char == ",":
                    char = "."
                if i == 0: # Isp
                    Isp[Run-1] = Isp[Run-1]+char
                if i == 1: # k
                    k[Run-1] = k[Run-1]+char
                if i == 2: # T*
                    T[Run-1] = T[Run-1]+char
                if i == 4: # c*
                    cstar[Run-1] = cstar[Run-1]+char
            else:
                if nextFlag == True:
                    i = i+1
                    nextFlag = False
            if i>=5:
                Isp[Run-1] = float(Isp[Run-1])
                k[Run-1] = float(k[Run-1])
                T[Run-1] = float(T[Run-1])
                cstar[Run-1] = float(cstar[Run-1])*0.3048
                print("Specific impulse: ", Isp[Run-1], " s")
                print("Isentropic exponent: ", k[Run-1])
                print("Total temperature: ", T[Run-1], " K")
                print("Characteristic velocity: ", cstar[Run-1], " m/s")
                break
        dataFlag = False


output = open("output.csv", "w")
writer = csv.writer(output)

rows = [["Run","Molecular weight", "Specific impulse", "Isentropic exponent", "Total temperature", "Characeteristic velocity"], 
        ["N/A","[g/mol]", "[sec]", "[-]", "[K]", "[m/s]"]]


for row in range(Run):
    rows.append([row+1, M[row], Isp[row], k[row], T[row], cstar[row]])
writer.writerows(rows)

file.close()
output.close()