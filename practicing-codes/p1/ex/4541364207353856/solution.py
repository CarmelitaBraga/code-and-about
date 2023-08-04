num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

lista = [num1, num2, num3, num4, num5]

if num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5:
    print('com duplicados')
elif num2 == num3 or num2 == num4 or num2 == num5:
    print('com duplicados')
elif num3 == num4 or num3 == num5:
    print('com duplicados')
elif num4 == num5:
    print('com duplicados')
else:
    print('sem duplicados')
