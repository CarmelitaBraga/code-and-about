def separates_letters(phrase):
    letters = []
    for letter in phrase:
        letters.append(letter)
    return letters


def reunites_sentence(list):
    sentence = ''
    for word in list:
        sentence += word
    return sentence


def encrypt_data(data):
    list_of_letters = separates_letters(data)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = []
    for i in range(len(list_of_letters)):
        if list_of_letters[i] in alphabet:
            j = alphabet.find(list_of_letters[i])
            letters.append(alphabet[(j+3) % 26])
        else:
            letters.append(list_of_letters[i])
    return reunites_sentence(letters)


def encrypt_data_with_step(data, step):
    list_of_letters = separates_letters(data)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = []
    for i in range(len(list_of_letters)):
        if list_of_letters[i] in alphabet:
            j = alphabet.find(list_of_letters[i])
            letters.append(alphabet[(j+step) % 26])
        else:
            letters.append(list_of_letters[i])
    return reunites_sentence(letters)


def decrypt_data(data):
    list_of_letters = separates_letters(data)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = []
    for i in range(len(list_of_letters)):
        if list_of_letters[i] in alphabet:
            j = alphabet.find(list_of_letters[i])
            letters.append(alphabet[(j-3) % 26])
        else:
            letters.append(list_of_letters[i])
    return reunites_sentence(letters)


option = input("(E)ncrypt data or (D)ecrypt data? ").upper()

if option.startswith('E'):
    phrase = input("Gimme a phrase for encryption: ")
    option2 = input("Do you want to set a step? (Y)es or (N)o? ").upper()
    
    if option2.startswith("Y"):
        step = int(input("Set the step: "))
        cipher = encrypt_data_with_step(phrase, step)
    else:
        cipher = encrypt_data(phrase)
    
    print(cipher)

elif option.startswith('D'):
    phrase = input("Gimme a phrase for decryption: ")
    cipher = decrypt_data(phrase)
    print(cipher)

else:
    print("Choose a valid option! :)")