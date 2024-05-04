import random

def _gg():
    ans=set()
    while True:
        ans.add(random.randint(0,9))
        if len(ans)==4:
            break
    return list(ans)

    
cc=1
anss=_gg()  
while True:
    aa=0
    bb=0
    nn=input("Guess(0:end): ")
    if nn=="0":
        break
    for ii in range(4):
        if int(nn[ii])==anss[ii] :
            aa=aa+1
        elif int(nn[ii]) in anss:
            bb=bb+1
    
    if aa==4:
        print("沒看過這種天才!!啊!!")
        ss=input("是否繼續遊戲(Y/N)??")
        if ss.upper()=="Y":
            anss=_gg()
            cc=1
            continue
        else:
            break
    print(cc,".",aa,"A",bb,"B")  
    cc=cc+1   
    





