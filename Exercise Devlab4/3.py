# อ่านค่าจากผู้ใช้
a = int(input())
b = int(input())
x = int(input())

if a<b :
    for i in range(a, b+1, x):
        print(i, end=' ')
elif a==b :
    print(a)
else:
    for i in range(a, b-1, -x):
        print(i, end=' ')