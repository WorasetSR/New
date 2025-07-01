import random

FI = input('Item : ')
SI = input('Item : ')
I = [FI,SI]
RT = random.sample(I, k=2)
print('Item ที่ได้คือออ : ',RT[0])
p = input(f'อยากได้ {RT[1]} ด้วยมั้ย อยากได้ก็จ่ายสิ(พิมพ์ pay) : ')
if p == "pay" :
    print(f'ยินดีด้วยคุณได้ {RT[1]} แล้ว')

