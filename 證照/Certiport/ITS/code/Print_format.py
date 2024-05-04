# 格式化輸出

name = "ted"
score = 94.5

print("1 %s 的分數是 %.2f" % (name, score))
print()

print("2 {} 的分數是 {}".format(name, score))
print()

print("3 {0} 的分數是 {1}".format(name, score))
print()

print("4 {:8s} 的分數是 {:.2f}".format(name, score))
print()

print("5 {:8s} 的分數是 {:.2f}".format(name, score))
print()

print("6 {:>8s} 的分數是 {:.2f}".format(name, score))   #靠右對齊
print()

print("7 {:^8s} 的分數是 {:.2f}".format(name, score))   #置中對齊
print()

print("8 {0:8s} 的分數是 {1:.2f}".format(name, score)) 
print()

print(f"9 {name:8s} 的分數是 {score:.2f}") 
print()

print(10, format(name, "4s"),"的分數是", format(score,".2f")) 
print()