def isValid(cur):
    """Check if the list does not form a palindrome-like structure."""
    for i in range(len(cur) // 2):
        if cur[i] == cur[len(cur) - i - 1]:
            return False
    return True

def permut(cur, conj, used, i):
    """Backtracking function to generate valid permutations."""
    n = len(conj)

    if i == n:
        print(cur)  # Print valid sequence
        return

    for j in range(n):
        if used[j]:  # Skip already used elements
            continue

        new_cur = cur[:]  # Copy to avoid modifying parent recursion state
        new_cur[i] = conj[j]
        
        if isValid(new_cur):  # Only proceed if valid
            used[j] = True
            permut(new_cur, conj, used, i + 1)
            used[j] = False  # Backtrack

# Example call
n = 3
permut([""] * n, [1, 2, 3], [False] * n, 0)



# def perm(inp, cur, out):
#     if len(cur) == len(inp):
#         out.append(cur[:])
#         return
#     for i in range(len(inp)):
#         cur.append(inp[i])
#         print(cur)
#         perm(inp[:i]+inp[i+1:], cur, out)
#         cur.pop()
        
# perm([1,2,3], [], [])
        

# def dfs(inp, cur, out):
#     out.append(cur[:])
    
#     for i in range(len(inp)):
#         cur.append(inp[i])
#         dfs(inp[i+1:], cur, out)
#         cur.pop()
    
#     return out


# inp, cur, out = [1,2,3,4], [], []
# print(dfs(inp, cur, out))


# def permutation(inp, cur, out):
#     out.append(cur[:])
    
#     for i in range(len(inp)):
#         cur.append(inp[i])
#         dfs(inp[i+1:], cur, out)
#         cur.pop()
    
#     return out


# inp, cur, out = [1,2,3,4], [], []
# print(dfs(inp, cur, out))

