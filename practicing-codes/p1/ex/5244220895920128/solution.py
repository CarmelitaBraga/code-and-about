ref = int(input())

s = 0

for nums in range(10):
    num = int(input())
    if num % ref == 0:
        s += num

print(s)
