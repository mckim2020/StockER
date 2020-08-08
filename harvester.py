# Harvest data from excel file(종가, 거래량, 외국인, 기관, target: 등락률)
df = pd.read_excel("../input/stockdata-test/SKT.xlsx")

# Creating input data tensor

def dataToTens(n): 
    # nth row of stock dataset
    # [[PRICE, INST], [TRADE, FORN]]
    
    inTens = torch.empty(1, 1, 32, 32)
    
# view()를 이용한 크기 조절은 나중에 다시 해볼 것 
#     inTens[0, 0, 0, 0] = df.at[n, 'PRICE']
#     inTens[0, 0, 0, 1] = df.at[n, 'INST']
#     inTens[0, 0, 1, 0] = df.at[n, 'TRADE']
#     inTens[0, 0, 1, 1] = df.at[n, 'FORN']
#     inTens = inTens.view(1, -1)
    
    # 32 by 32 의 image 로 데이터를 변환 
    valP = df.at[n, 'PRICE']
    for i in range(0,16):
        for j in range(0,16):
            inTens[0, 0, i, j] = float(valP) / 100000

    valT = df.at[n, 'TRADE']
    for i in range(16,32):
        for j in range(0,16):
            inTens[0, 0, i, j] = float(valT) / 100000
        
    valI = df.at[n, 'INST']
    for i in range(0,16):
        for j in range(16,32):
            inTens[0, 0, i, j] = float(valI) / 100000
        
    valF = df.at[n, 'FORN']
    for i in range(16,32):
        for j in range(16,32):
            inTens[0, 0, i, j] = float(valF) / 100000

    targetTens = torch.empty(1, 10)
    targetTens[0,:] = float(df.at[n, 'UPDOWN']) * 100 
    targetTens.view(1, -1)
    
#     print(inTens)
#     print(targetTens)
    return inTens, targetTens

