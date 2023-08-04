def coincident_letters(p1, p2):
    min_factor = len(p1) if len(p1) <= len(p2) else len(p2)
    cont = 0

    print('Letras coincidentes')

    for i in range(min_factor):

        if p1[i] == p2[i]:
            cont += 1
            print(f"'{p1[i]}' na posição {i+1}")

    calc = (cont/(len(p1) + len(p2)))*100

    print(f'Total de letras coincidentes: {cont} ({calc:.0f}%)')

def main():
    x = str(input())
    y = str(input())

    coincident_letters(x, y)

if __name__ == '__main__':
    main()

