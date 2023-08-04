mparcial = float(input())
final = 0
mfinal = 0

while not mfinal >= 5:
    final += 0.01
    mfinal = (mparcial*0.6) + (final*0.4)

print(f'{final:.1f}')

