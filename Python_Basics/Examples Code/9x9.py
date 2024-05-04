# 打印九九乘法


def nine_to_nine():
    for i in range(1, 10):
        for j in range(1, 10):
            print(i, "*", j, "=", i * j, " ", end=" ")
        print("\n")


def _9x9():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} x {j} = {i*j}", end="\t")
        print()


nine_to_nine()
# _9x9()
