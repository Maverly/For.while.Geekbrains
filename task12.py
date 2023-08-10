print ('Введите сумму и произведение задуманных чисел')
s=int(input())
p=int(input())
for x in range(1001):
    for y in range(1001):
        if x+y==s and x*y==p:
            print(x,y)
            exit()