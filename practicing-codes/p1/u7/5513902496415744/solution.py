def slicer(start, end, lista):
    nova_lista = []
    for j in range(start, start + end):
        nova_lista.append(lista[j])
    return nova_lista


def is_substring(word, seq):
    array_seq = []
    array_word = []
    array_seq += seq
    array_word += word
    for i_word in range((len(word) - len(seq)) + 1):
        #intervalo = []
        intervalo = (slicer(i_word, len(seq), array_word))
        if array_seq == intervalo:
            print(intervalo)
            return True
    print('não é substring')
    return False

print(is_substring('answering', 'ring'))
print(is_substring('bowling', 'owl'))
print(is_substring('axiomatic', 'axioma'))
print(is_substring('casorio', 'casa'))


#bowling / owl
#answering / ring
#axiomatic / axioma
#forgiveness/ give
#hometown / own

def slicer(start, end, lista):
    nova_lista = []
    for j in range(start, end):
        nova_lista.append(lista[j])
    return nova_lista
        

def is_substring(word, seq):
    array_seq = []
    array_word = []
    array_seq += seq
    array_word += word
    for i_word in range(len(word) - len(seq)):
        intervalo = []
        intervalo.append(slicer(i_word, len(seq), array_word))
        for i_seq in range(len(seq)):
            if array_seq == intervalo:
                print(intervalo)
                return True
    print('não é substring')
    return False

'''
def test_1():
    palavra1 = 'bowling'
    chave1 = 'owl'
    assert is_substring(palavra1, chave1) == True

def test_2():
    palavra2 = 'answering'
    chave2 = 'ring'
    assert is_substring(palavra2, chave2) == True

def test_3():
    palavra3 = 'axiomatic'
    chave3 = 'axioma'
    assert is_substring(palavra3, chave3) == True

def test_4():
    palavra4 = 'casorio'
    chave4 = 'casa'
    assert not is_substring(palavra4, chave4) == True
'''
print(is_substring('answering', 'ring'))
print(is_substring('bowling', 'owl'))
print(is_substring('axiomatic', 'axioma'))
print(is_substring('casorio', 'casa'))
         

        








#procurar a primeira letra e checar se dá match

'''def substring(palavra, sequencia):
    soma = 0
    for i in range(len(palavra)):
        if palavra[i] == sequencia[0]:
            if palavra[i:len(sequencia) - soma] == sequencia:
                print(sequencia)
            soma += 1

x = substring('bowling', 'owl')
y = substring('axiomatic', 'axioma')'''
