import random
from time import sleep
list = ['innocence', 'guilt']
listf = ['innocent', 'guilty']
computer = random.choice(list)
computerf = random.choice(listf)
print('Police officer: \033[1;31mYour friend has delated you. What do you have to say?\033[m')
sleep(2)
person = str(input('\033[1;97mAre you guilty?[Y/N] \033[m')).lower().strip()[0]
personc = str(input('\033[1;97mIs your friend innocent or guilty?[I/G] ')).strip().lower()[0]
sleep(1)
print(f'The friend claimed {"being innocent" if computer == "innocence" else "being guilty"}.')
sleep(1)
print(f'You claimed {"innocence" if person == "n" else "you are guilty"}.')
sleep(1)
print(f'Your friend claimed you are {"innocent" if computerf == "innocent" else "a criminal"}.')
sleep(1)
print(f'You affirmed your friend is {"culpable" if personc == "g" else "innocuous"}.\033[m')
sleep(2)
print('Police officer: \n\033[7;57m')
if computer == 'innocence' and computerf == 'innocent':
    if person == 'n' and personc == 'i':
        print('You guys are safe.')
    if person == 'n' and personc == 'g':
        print('Thank you for your contribution, we have to talk to your friend.')
    if person == 'y' and personc == 'i':
        print('You are arrested, follow me.')
    if person == 'y' and personc == 'g':
        print('Thank you for your contribution. Your friend is busted.')
if computer == 'innocence' and computerf == 'guilty':
    if person == 'n' and personc == 'i':
        print('We have to do some trial, you are arrested.')
    if person == 'n' and personc == 'g':
        print('Thank you for your contribution, you are both arrested.')
    if person == 'y' and personc == 'i':
        print('You are arrested, but with a reduced sentence for contribution.')
    if person == 'y' and personc == 'g':
        print('Thank you for your contribution, we have to talk to your friend.')
if computer == 'guilt' and computerf == 'guilty':
    if person == 'n' and personc == 'i':
        print('It is a lie. You both will be arrested, but your friend will have the sentence reduced')
    if person == 'n' and personc == 'g':
        print('You are busted.')
    if person == 'y' and personc == 'i':
        print('Thank you for your contribution. Part of it is a lie though.')
    if person == 'y' and personc == 'g':
        print('Thank you for your contribution. The judge has the discretion to impose a lesser sentence on you both.')
if computer == 'guilt' and computerf == 'innocent':
    if person == 'n' and personc == 'i':
        print('Thank you for your contribution. Part of it is a lie though. \nYour friend is arrested.')
    if person == 'n' and personc == 'g':
        print('You are free. Thanks for you contribution. \nYour friend is busted.')
    if person == 'y' and personc == 'i':
        print('You are both busted.')
    if person == 'y' and personc == 'g':
        print('Your friend lied, now is busted. \nYou are arrested, but your sentence will decrease.')
print('\033[m')






'''import math
x = int(input('Quadrados preenchidos: '))
a = 0
for c in range(1, x + 1):
    y = math.pow(2, c)
    a += y
print(f'A soma total é {a} grãos.')'''