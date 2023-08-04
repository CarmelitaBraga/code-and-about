'''from time import sleep

def gostarDeCarmelita(coeficienteDeAmor):
    coeficienteDeAmor += 1
    return coeficienteDeAmor

CarmEficient = 0
while True:
    print(f'Atualmente: {CarmEficient}%')
    sleep(0.1)
    gostarDeCarmelita(CarmEficient)'''

'''def gostarDeCarmelita(C):
    print(C)
    if C < 10**2:
        return f"{(C + gostarDeCarmelita(C+1))}"

x = 0
print(f"Sentimento atual: {gostarDeCarmelita(x)}")'''

'''def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 8
print("The factorial of", num, "is", factorial(num))'''