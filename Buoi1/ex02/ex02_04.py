j=[]
a = int(input("Nhập số chia hết: "))
b = int(input("Nhập số không chia hết:"))
for i in range(2000, 3201):
    if(i % a == 0) and (i % b != 0):
        j.append(str(i))
print(','.join(j))