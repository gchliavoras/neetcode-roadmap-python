class Solution:
#Valid Sudoku
#You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
#Each row must contain the digits 1-9 without duplicates.
#Each column must contain the digits 1-9 without duplicates.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
#Return true if the Sudoku board is valid, otherwise return false
#Note: A board does not need to be full or be solvable to be valid.
  def isValidSudoku(self, board: list[list[str]]) -> bool:
    temp = []
    for row in board: #for each row
      test = [element for element in row if element != "."] #Fill test array with filtered row elements
      if len(set(test)) != len(test): #Check for duplicates
        print("rows")
        return False
    for i in range(9): #for each column
      for row in board:
        temp.append(row[i]) #Fill array with unfiltered column elements
      test = [element for element in temp if element != "."] #Fill test array with filtered column elements
      temp = []
      if len(set(test)) != len(test): #test for duplicates
        print("columns")
        return False
    for m in range(3): #cell rows
      for n in range(3): #cell columns
        for row in board[3*m:3*m+3]:
          temp.extend(row[3*n:3*n+3]) #Fill array with unfiltered cell elements of each row
        test = [element for element in temp if element != "."] #Fill test array with filtered cell elements
        if len(set(test)) != len(test): #test for duplicates
          print("cells")
          return False
        temp = []
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