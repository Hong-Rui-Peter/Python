def getRoom(student, year):
    #為學生分配場地
    if year == 1:
        print(f"\n{student.title()}, 請到 第一會議室 報到")
    elif year == 2:
        print(f"\n{student.title()}, 請到 第二會議室 報到")
    elif year == 3:
        print(f"\n{student.title()}, 請到 視聽教室 報到")
    elif year == 4:
        print(f"\n{student.title()}, 請到 禮堂 報到")
    elif year == 5:
        print(f"\n{student.title()}, 請到 音樂教室 報到")
    else:
        print(f"\n{student.title()}, 請到 風雨操場 報到")
        
name = input("請輸入您的姓名：")
grade = 0
while grade not in (1,2,3,4,5,6):
    grade = int(input("請輸入年級： (1~6) ? "))

getRoom (name, year = grade) 
getRoom ("guido rossum", 3)
getRoom (year = 6, name="Guido Rossum")
#getRoom (year = 6, student="Guido Rossum")