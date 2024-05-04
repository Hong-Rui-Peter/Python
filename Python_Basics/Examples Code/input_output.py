# 基本出入輸出+string不同格式

def input_print():
    name = input("請輸入名子:")
    print(name, "好帥")
    print(f"{name}好帥")
    print("{}好帥".format(name))
    print("fuck python\n")


input_print()