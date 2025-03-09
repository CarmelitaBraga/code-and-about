string = input()
pattern = input()
has = False

for i in range(len(string)):
    has = False
    tmp = i
    for j in range(len(pattern)):
        # print(string[tmp], pattern[j])
        if tmp < len(string) and string[tmp] == pattern[j]:
            tmp += 1
        else:
            break

    if j == len(pattern)-1 and string[i:i+j+1] == pattern:
        has = True
        break
    
print(has)