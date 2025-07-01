h = float(input("ค่าเช่าบ้าน : "))
w = float(input("ค่าน้ำ : "))
e = float(input("ค่าไฟ : "))
n = float(input("ค่าเน็ต : "))
p = float(input("ค่าโทรศัพท์ : "))
money = 2000
moneyn = 2000 - h - w - e - n - p
print(f'''เงินเหลือ {money} ต้องการซื้ออะไร
1. บะหมี่กึ่งสำเร็จรูปเส้นเหนียวนุ่ม (chewy noodles) 10 บาท
2. บะหมี่กึ่งสำเร็จรูปธรรมดา (instant noodles) 6 บาท
3. น้ำซุปบะหมี่กึ่งสำเร็จรูป (soup) 2 บาท
4. น้ำประปาดื่มได้ (drinking water) 0 บาท''')
shop = int(input("เลือก : "))
if shop == 1:
    print(f"เหลือ {moneyn-10} บาท")
elif shop == 2:
    print(f"เหลือ {moneyn-6} บาท")
elif shop == 3:
    print(f"เหลือ {moneyn-2} บาท")
elif shop == 4:
    print(f"เหลือ {moneyn} บาท")
else:
    print("error")