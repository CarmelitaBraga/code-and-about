'''while True:
    students = []
    N = int(input())

    if N == 0:
        break

    for _ in range(N):
        students.append(input().split())
        
    i = 0
    token = int(students[i][1])

    while len(students) > 1:
        old_i = i
        position = token % len(students)

        if token % 2 == 0:
            i = (old_i + position - 1) % len(students)
            student, token = students.pop(i)
            token = int(token)
        else:
            i = ((-1 * position) + old_i) % len(students)
            student, token = students.pop(i)
            token = int(token)

    print(f'Vencedor(a): {students[0][0]}')'''

winners = []

while True:
    students = []
    N = int(input())

    if N == 0:
        break

    for _ in range(N):
        students.append(input().split())
        
    i = 0
    token = int(students[i][1])

    while len(students) > 1:
        old_i = i
        position = token % len(students)

        if token % 2 == 0:
            i = (old_i + position - 1) % len(students)
            student, token = students.pop(i)
            token = int(token)
        else:
            i = ((-1 * position) + old_i) % len(students)
            student, token = students.pop(i)
            token = int(token)

    winners.append(students[0][0])

for winner in winners:
    print(f'Vencedor(a): {winner}')
