# Creating input data tensor from excel file using pandas library
# 지정 file의 n번째 줄의 데이터로 1 by 1 by 32 by 32 tensor를 만듦

import pandas as pd


def dataToTens(n, file): 
    # nth row of stock dataset
    # [[PRICE, INST], [TRADE, FORN]]
    
    inTens = torch.empty(1, 1, 32, 32)
    
# view()를 이용한 크기 조절은 나중에 다시 해볼 것 
#     inTens[0, 0, 0, 0] = file.at[n, 'PRICE']
#     inTens[0, 0, 0, 1] = file.at[n, 'INST']
#     inTens[0, 0, 1, 0] = file.at[n, 'TRADE']
#     inTens[0, 0, 1, 1] = file.at[n, 'FORN']
#     inTens = inTens.view(1, -1)
    
    # 32 by 32 의 image 로 데이터를 변환 
    valP = file.at[n, 'INST']
    for i in range(0,16):
        for j in range(0,16):
            inTens[0, 0, i, j] = float(valP) / 100000

    valT = file.at[n, 'FORN']
    for i in range(16,32):
        for j in range(0,16):
            inTens[0, 0, i, j] = float(valT) / 100000
        
    valI = file.at[n+1, 'INST']
    for i in range(0,16):
        for j in range(16,32):
            inTens[0, 0, i, j] = float(valI) / 100000
        
    valF = file.at[n+1, 'FORN']
    for i in range(16,32):
        for j in range(16,32):
            inTens[0, 0, i, j] = float(valF) / 100000

    targetTens = torch.zeros(1, 8)
    # 우상향 그래프
    if file.at[n-1, 'UPDOWN'] > 0:
        for i in range(4):
            targetTens[0, i] = -1
            
    # 좌상향 그래프
    else:
        for i in range(4):
            targetTens[0, i] = 1

    return inTens, targetTens

