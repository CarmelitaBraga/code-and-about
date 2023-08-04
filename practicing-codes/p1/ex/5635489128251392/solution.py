lim = float(input())
num = 0

while True:
    num += 1
    if num >= lim: break
    if num % 2 == 0 and num % 5 == 0 and num > 0:
        print(num)
