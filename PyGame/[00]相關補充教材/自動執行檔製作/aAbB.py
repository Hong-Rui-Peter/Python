'''
幾A幾B--自訂函示版(list)--示範程式
'''
def _aaBB():
    lisT=list()
    while True:
        aB=random.randint(0,9)
        if aB not in lisT:
            lisT.append(aB)
        if len(lisT)==4:
            break
    return(lisT)        

    
import random

nAnB=_aaBB()
cC=1
while True:
    aA=0
    bB=0
    nN=input("請猜四個數字(0-結束): ")
    if nN=="0":
        break
    
    gG=list(nN)
    for vI in range(4):
        if nAnB[vI]==int(gG[vI]):
            aA=aA+1
        elif int(gG[vI]) in nAnB:
            bB=bB+1
    print(cC,".",aA,"A",bB,"B")
    if aA==4:
        print("恭喜老爺!!賀喜夫人!!")
        yN=input("再玩一次(Y/N)?? ")
        if yN.upper()=="Y":
            cC=1
            nAnB=_aaBB()
            continue
        else:
            break
    cC=cC+1
         
            
         
            