# def solve_n_queens(n):
#     count = 0
#     def backtrack(linha):
#         if linha == n:
#             print(board)
#             count += 1
#             return
        
#         for j in range(n):
#             if (j in columns or abs(linha-j) in negative_diagonals or (linha+j) in positive_diagonals):
#                 continue

#             columns.add(j)
#             negative_diagonals.add(linha - j)
#             positive_diagonals.add(linha + j)
#             board[linha][j] = 'Q'

#             backtrack(linha+1)
            
#             columns.remove(j)
#             negative_diagonals.remove(linha - j)
#             positive_diagonals.remove(linha + j)
#             board[linha][j] = '.'
    
#     board = [["." for _ in range(n)] for _ in range(n)]
#     columns, negative_diagonals, positive_diagonals = set(), set(), set()
#     backtrack(0)
#     return count

# n = int(input())
# print(solve_n_queens(n))
# # for row in solve_n_queens(n):
# #     # for row in solution:
# #     print(row)
# #     # print()
    
    
    
    
    
    
    
    
    
    
#     # for i in range(line):
#     #     if board[i][column] == 'Q':
#     #         return False
        
#     #     if board[line][i] == 'Q':
#     #         return False
        
#     #     if board[abs(line-i)][abs(column-i)] == 'Q':
#     #         return False
        
#     #     if board[abs(line-i)][abs(column+i)] == 'Q':
#     #         return False
        
#     #     if board[abs(line+i)][abs(column-i)] == 'Q':
#     #         return False
        
#     #     if board[abs(line+i)][abs(column+i)] == 'Q':
#     #         return False
#     # return True



def solve_n_queens(n):
    def backtrack(row, cols, diag1, diag2, board):
        if row == n:  # All queens placed
            solutions.append(["".join(row) for row in board])
            return
        
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue  # Conflict, skip this column
            
            # Place queen
            board[row][col] = 'Q'
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            
            backtrack(row + 1, cols, diag1, diag2, board)
            
            # Backtrack (remove queen)
            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    solutions = []
    empty_board = [["." for _ in range(n)] for _ in range(n)]
    backtrack(0, set(), set(), set(), empty_board)
    return solutions

n = 4
for solution in solve_n_queens(n):
    for row in solution:
        print(row)
    print()
