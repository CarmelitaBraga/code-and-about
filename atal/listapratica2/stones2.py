def valid_op1(a, b, c): return a >= 1 and b >= 2
def valid_op2(a, b, c): return b >= 1 and c >= 2

def junta_pedra(a, b, c):
    op2 = min(b, c//2) if valid_op2(a,b,c) else 0
    b -= op2
    op1 = min(a, b//2) if valid_op1(a,b,c) else 0
    if op1:
        op = op1 + op2
    else:
        op = max(op1, op2)
    return op*3


n = int(input())
res = ''

for _ in range(n):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    
    res += str(junta_pedra(a, b, c)) + '\n'
    
print(res.strip())