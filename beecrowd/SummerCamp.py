#students = [['A', 7], ['B', 2], ['C', 6], ['D', 5], ['E', 1], ['F', 8]]
students = []
N = int(input())
for _ in range(N):
    students.append(input().split())
    
i = 0
token = int(students[i][1])
#position = token % len(students)

while len(students) > 1:
    old_i = i
    position = token % len(students)

    if token % 2 == 0:
        i = (old_i + position - 1) % len(students)
        student, token = students.pop(i)
        token = int(token)
    else:
        i = ((-1 * position) + old_i) % len(students)
        #token = int(students[i][1])
        student, token = students.pop(i)
        token = int(token)

print(f'Vencedor(a): {students[0][0]}')
