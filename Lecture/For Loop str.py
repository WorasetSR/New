p = ["poom", "nam", "kay"]
for a in p :
    print(a)

x = int(input('Number : '))
print(x*"*")
text = ''


for b in range(x) :
    if b == x-1 :
        print('*')
        break
    print('*', end='')



for c in range(x) :
    text += '*'
print(text)


for d in range(x) :
    print((d+1)*"*")