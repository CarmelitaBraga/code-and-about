num = int(input())

while True:
    if num // 10 == 0:
        print(num % 10)
        break
    else:
        x = num % 10
        print(x)
        num = num // 10
