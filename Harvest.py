import openpyxl
from math import sqrt


# Constants (for NAVER only)
instVar = 6583559856
fornVar = 12242265201

# Load files
f = "C:/Users/HOME/Desktop/네이버.xlsx"
book = openpyxl.load_workbook(f)
sheet = book['Sheet1']

# Probability density function
F_inst = {}
F_forn = {}
F_instforn = {}

# Counting elements and calculate density
# Inst PDF
for row in sheet['C']:
    i = str(row.value)

    if i not in F_inst:
        F_inst[i] = 1/400
    else:
        F_inst[i] += 1/400

# Forn PDF
for row in sheet['D']:
    f = str(row.value)

    if f not in F_forn:
        F_forn[f] = 1/400
    else:
        F_forn[f] += 1/400

# Muliplied PDF
for row1 in sheet['C']:
    for row2 in sheet['D']:
        p = str(int(row1.value) * int(row2.value))

        if p not in F_instforn:
            F_instforn[p] = (1/400)**2
        else:
            F_instforn[p] += (1/400)**2

# Calculate E[inst], E[forn], E[mul]
E_inst = 0
E_forn = 0
E_mul = 0

for key, val in F_inst.items():
    E_inst += int(key) * val

for key, val in F_forn.items():
    E_forn += int(key) * val

for key, val in F_instforn.items():
    E_mul += int(key) * val

# print(E_inst, E_forn, E_mul)

cov = E_mul - E_inst * E_forn
corr = cov / sqrt(instVar * fornVar)
print(corr)
