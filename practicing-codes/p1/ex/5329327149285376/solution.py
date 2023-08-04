from math import sqrt

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

d12 = sqrt((x1-x2)**2 + (y1-y2)**2)
d13 = sqrt((x1-x3)**2 + (y1-y3)**2)
d23 = sqrt((x2-x3)**2 + (y2-y3)**2)

per = d12 + d13 + d23

print(f'O perímetro é de {per:.2f}')
