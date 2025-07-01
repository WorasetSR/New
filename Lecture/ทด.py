start = int(input("Start: "))  # รับค่าตัวเริ่มต้น
step = int(input("Step: "))    # รับค่าระยะห่างของแต่ละตัว
result = ''
for i in range(5):  # วนซ้ำ 5 รอบ
    result += str(start+step*i+1)
print(result)