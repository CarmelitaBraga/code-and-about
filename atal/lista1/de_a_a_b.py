def op1(a):
    return 2*a

def op2(a):
    return 10 * a + 1


def fromatob(a, b):
    
    def backtrack(a, b, lista):
        lista.append(a)
        if a == b:
            # lista.append(a)
            # print("HERE", lista)
            return True, lista

        elif a > b:
            lista.pop()
            return False, lista

        else:
            print(lista)
            res1, lista = backtrack(op1(a), b, lista)
            
            if not res1:
                res2, lista = backtrack(op2(a), b, lista)
            if not res1 and not res2:
                lista.pop()
    
    return backtrack(a, b, [])


a, b = input().split()
a, b = int(a), int(b)

print(fromatob(a, b))


