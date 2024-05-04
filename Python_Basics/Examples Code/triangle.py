# 執行: python  my_python.py
# 輸出三角形+python語言敘述

def space(n):
    for spc in range(n):
        print(" ", end="")

def space2(n):
    for spc in range(1,n+1):
        print(" ", end="") 
        

if __name__ == "__main__":

    for x in range(1,7):
        space2(6-x)
        
        for y in range(1,x*2):
            print("*", end="")
        print()
    
    print("\nPython 是直譯式程式語言")
    print("採邊翻譯邊執行的方式")
    