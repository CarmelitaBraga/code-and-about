def separating_numbers(num):    
    total = num - (num % 10)
    print(num%10)

    while True:
        a = total % 100
        print(a)
        total -= a
        if total == 100:
            print(1)
            break
        if total < 100:
            a = total % 10
            print(a)
        if total // 10 == 0:
            a = total % 10
            print(a)
            break
        

def main():
    separating_numbers(int(input()))

if __name__ == '__main__':
    main()


        #cont += 1
        #vai multiplicar por 10




    '''if num < 10:
       w = num % 10
       

    elif 10 <= num < 100:
       w = num % 10
       v = num // 10
       print(w, '\n', v)

    elif 100 <= num < 1000:
        

    elif 1000 <= num < 10000:'''
