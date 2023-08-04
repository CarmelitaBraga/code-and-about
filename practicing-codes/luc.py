def ask(i, j):
    print(f'? {i} {j}',flush=True)
    res = int(input())
    return res

n = int(input())

a = ask(1,2)
b = ask(1,3)
c = ask(2,3)

x = (a + b - c) // 2
y = a - x
z = b - x
resp = f'{x} {y} {z}'
for i in range(4,n+1):
    resp += " " + str(ask(1,i) - x)

print("! " + resp, flush=True)
