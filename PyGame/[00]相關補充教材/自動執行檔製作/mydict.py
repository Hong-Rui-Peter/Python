mydd={}
while True:
    ee=input("English: ")
    if ee=="0":
        break
    elif ee=="pp":
        for ii in mydd.items():
            print(ii)
    elif ee=="dd":
        dd=input("Which to kill: ")
        if mydd.get(dd)==None:
            print("Not found!!")
        else:
            del mydd[dd]
            print("Killed!!")
    elif ee=="uu":
        uu=input("Which to update: ")
        if mydd.get(uu)==None:
            print("Not found!!")
        else:
            cc=input("Chinese: ")
            mydd[uu]=cc
            print("Update Compeleted!!")
    elif mydd.get(ee)==None:
        cc=input("Chinese: ")
        mydd[ee]=cc
    else:
        print("Chinese is: ",mydd[ee])

