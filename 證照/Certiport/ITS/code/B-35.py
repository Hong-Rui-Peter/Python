import datetime

print('DateTime:', datetime.datetime.now())
print('Date:', datetime.datetime.now().date())
print('Time:', datetime.datetime.now().time())

update_time=datetime.datetime.now()
print(update_time.strftime("%A")) #星期

print(update_time.strftime("%B")) #月份

print(update_time.strftime("%M")) #分鐘

'''
%y 兩位數的年份表示（00-99）

%Y 四位數的年份表示（000-9999）

%m 月份（01-12）

%d 月內中的一天（0-31）

%H 24小時制小時數（0-23）

%I 12小時制小時數（01-12）

%M 分鐘數（00=59）

%S 秒（00-59）

%a 本地簡化星期名稱

%A 本地完整星期名稱

%b 本地簡化的月份名稱

%B 本地完整的月份名稱

%c 本地相應的日期表示和時間表示

%j 年內的一天（001-366）

%p 本地A.M.或P.M.的等價符

%U 一年中的星期數（00-53）星期天為星期的開始

%w 星期（0-6），星期天為星期的開始

%W 一年中的星期數（00-53）星期一為星期的開始

%x 本地相應的日期表示

%X 本地相應的時間表示

%Z 當前時區的名稱

%% %號本身
'''