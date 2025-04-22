class Solution:
#Valid Sudoku
#You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
#Each row must contain the digits 1-9 without duplicates.
#Each column must contain the digits 1-9 without duplicates.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
#Return true if the Sudoku board is valid, otherwise return false
#Note: A board does not need to be full or be solvable to be valid.
  def isValidSudoku(self, board: list[list[str]]) -> bool:
    rows: list[set[int]] = [set() for _ in range(9)]
    cols: list[set[int]] = [set() for _ in range(9)]
    cells: list[set[int]] = [set() for _ in range(9)] #123|456|789
    
    for m in range(9):
      for n in range(9):
        try: 
          element = int(board[m][n])
        except ValueError:
          continue
        cell_index = 3 * (m // 3) + n // 3 # //: floor of division
        if element in rows[m] or element in cols[n] or element in cells[cell_index]:
          return False
        rows[m].add(element)
        cols[n].add(element)
        cells[cell_index].add(element)
    return True

input_boards = [ 
  [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
  ],
  [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","1",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
  ]
]

if __name__ == "__main__":
  solution = Solution()
  for input_board in input_boards:
    print(solution.isValidSudoku(input_board))