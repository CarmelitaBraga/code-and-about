def inverte3a3(s):
    nova_string = ''
    for i in range(len(s) - 1, 0, -3):
        nova_string += s[i - 2] + s[i - 1] + s[i]
    return nova_string

