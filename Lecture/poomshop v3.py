menu = {'a':10 , 'b':20 , 'c':30}
summary = []
def oderr() :
    while True :
        oder = input('สั่งของ : ')
        if oder.lower() == 'exit' :
            break
        else:
            summary.append([oder,menu[oder]])
def bill() :
    total = 0
    print('Bill'.center(20, '-'))
    for i in range(len(summary)) :
        print(summary[i][0], summary[i][1], 'Bath')
        total += summary[i][1]
    print('Total :', total)

oderr()
bill()