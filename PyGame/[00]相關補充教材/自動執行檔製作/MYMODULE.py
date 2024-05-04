'''
自訂模組的示範程式
'''
import random
import time

def _cDate(daY):
    dayList=daY.split("/")
    if len(dayList[1])<2 and len(dayList[2])<2:
        myDate="中華民國"+str(int(dayList[0])-1911)+"年0"+dayList[1]+"月0"+dayList[2]+"日"
    elif len(dayList[1])<2:
        myDate="中華民國"+str(int(dayList[0])-1911)+"年0"+dayList[1]+"月"+dayList[2]+"日"
    elif len(dayList[2])<2:
        myDate="中華民國"+str(int(dayList[0])-1911)+"年"+dayList[1]+"月0"+dayList[2]+"日"
    else:    
        myDate="中華民國"+str(int(dayList[0])-1911)+"年"+dayList[1]+"月"+dayList[2]+"日"
    return(myDate)
    
    
def _sDate(daY):
    dayList=daY.split("/")
    myDate=str(int(dayList[0])-1911)+"年"+str(int(dayList[1]))+"月"+str(int(dayList[2]))+"日"
    return(myDate)

def _myHead():
    heaD=[{"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"},
          {"user-agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"},
          {"user-agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}]
    return(heaD[random.randint(0,len(heaD)-1)])
    
def _saying():
    saY=["~~心開就開心~~",
         "~~樹大必有枯枝，人多必有白痴~~",
         "~~塞翁失馬，焉知非福~~",
         "~~禍福相倚~~",
         "~~世界如舞台，你我只不過是個演員~~",
         "~~沒有口水與汗水，就沒有成功的淚水~~",
         "~~成功在優點的發揮，失敗是缺點的累積~~",
         "你不一定要很厲害，才能開始；但你要開始，才能很厲害",
         "沒有退路時，潛能就發揮出來了",
         "永不言敗，是成功者的最佳品格",
         "要成功，先發瘋，頭腦簡單向前衝"
        ]
    return(saY[random.randint(0,len(saY)-1)])
        

def _today():
    daY=time.localtime()
    weeK=["一","二","三","四","五","六","日"]
    toDay="民國"+str(daY.tm_year-1911)+"年"+str(daY.tm_mon)+"月"+str(daY.tm_mday)+"日"+"星期"+str(weeK[daY.tm_wday])
    return(toDay)

def _now():
    daY=time.localtime()
    if daY.tm_hour>=12:
        houR="下午"+str(daY.tm_hour-12)
    else:
        houR="上午"+str(daY.tm_hour)
    noW=houR+"點"+str(daY.tm_min)+"分"+str(daY.tm_sec)+"秒"
    return(noW)


def _show(ss,tt=0.3):
    for ii in range(0,len(ss)):
        time.sleep(tt)
        print(ss[ii],end="")
    print()



    
    


    