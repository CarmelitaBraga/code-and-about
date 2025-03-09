def valid_op1(a, b, c): return a >= 1 and b >= a//2
def valid_op2(a, b, c): return b >= 1 and c >= b//2

def junta_pedra(a, b, c):
    def backtrack(a, b, c, total):
        if b == 0 or (not valid_op1(a, b, c) and not valid_op2(a, b, c)):
            return total
        
        if valid_op1(a, b, c):
            t = backtrack(a-(b//2), b%2, c, total+(b//2)+(b-(b%2)))
        if valid_op2(a, b, c):
            t = backtrack(a, b-(c//2), c%2, total+(c//2)+(c-(c%2)))
        return t
    
    total = 0
    return backtrack(a, b, c, total)


a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
print(junta_pedra(a, b, c))

# n = int(input())
# res = ''

# for _ in range(n):
#     a, b, c = input().split()
#     a, b, c = int(a), int(b), int(c)
    
#     res += str(junta_pedra(a, b, c)) + '\n'
    
# print(res.strip())