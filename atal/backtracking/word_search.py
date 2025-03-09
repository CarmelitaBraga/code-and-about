class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        
        LIN, COL = len(board), len(board[0])

        def backtrack(l, c, i):
            if i == len(word):
                return True

            if (l < 0 or c < 0 or 
                l >= LIN or c >= COL or
                board[l][c] != word[i]):
                return False
            
            tmp = board[l][c]
            board[l][c] = '#'
            
            found = (backtrack(l+1, c, i+1) or
                backtrack(l-1, c, i+1) or
                backtrack(l, c+1, i+1) or
                backtrack(l, c-1, i+1))

            board[l][c] = tmp
            return found

        for i in range(LIN):
            for j in range(COL):
                if board[i][j] == word[0] and backtrack(i, j, 0):
                    return True
        return False


# from typing import List

# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         if not board:
#             return False
        
#         ROWS, COLS = len(board), len(board[0])

#         def backtrack(r, c, i):
#             # Base case: Found the word
#             if i == len(word):  
#                 return True

#             # Boundary conditions and mismatch check
#             if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i]):
#                 return False

#             # Mark as visited
#             temp = board[r][c]
#             board[r][c] = '#'

#             # Explore all four directions
#             found = (backtrack(r+1, c, i+1) or
#                      backtrack(r-1, c, i+1) or
#                      backtrack(r, c+1, i+1) or
#                      backtrack(r, c-1, i+1))

#             # Undo the change (backtrack)
#             board[r][c] = temp
#             return found

#         # Try to find the word starting from each cell
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if board[r][c] == word[0] and backtrack(r, c, 0):
#                     return True
#         return False
