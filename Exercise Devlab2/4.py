import math

P = float(input("Price(Bath) : "))
D = float(input("เงินดาวน์ : "))
M = float(input("เงินผ่อนต่อเดือน : "))
print(math.ceil((P-D)/M))