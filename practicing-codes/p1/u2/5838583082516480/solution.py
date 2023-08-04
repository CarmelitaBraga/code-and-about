c1 = int(input())
c2 = int(input())
c3 = int(input())

print(f'{(c1-(c1%100))//100}-{c1%100}')
soma1 = (c1%100)//10 + c1%10
print(soma1)

print(f'{(c2-(c2%100))//100}-{c2%100}')
soma2 = (c2%100)//10 + c2%10
print(soma2)


print(f'{(c3-(c3%100))//100}-{c3%100}')
soma3 = (c3%100)//10 + c3%10
print(soma3)


