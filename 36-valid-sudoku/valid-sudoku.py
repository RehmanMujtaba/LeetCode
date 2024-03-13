class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isValidSection(sec: List[str]) -> bool:
            hp = set()
            print(sec)
            for num in sec:
                if (num in hp) and (num != "."):
                    return False
                else:
                    hp.add(num)
            return True
        
        for row in board:
            if not isValidSection(row):
                return False

        for i in range(0,9):
            lst = []
            for j in range(0,9):
                lst.append(board[j][i])
            if not isValidSection(lst):
                return False
        lst = []
        j = 0
        for i in range(0,3):
            lst.append(board[i][j + 0])
            lst.append(board[i][j + 1])
            lst.append(board[i][j + 2])
        if not isValidSection(lst):
            return False
        lst = []
        j = 3
        for i in range(0,3):
            lst.append(board[i][j + 0])
            lst.append(board[i][j + 1])
            lst.append(board[i][j + 2])
        if not isValidSection(lst):
            return False
        lst = []
        j = 6
        for i in range(0,3):
            lst.append(board[i][j + 0])
            lst.append(board[i][j + 1])
            lst.append(board[i][j + 2])
        if not isValidSection(lst):
            return False
        lst = []
        j = 0
        for i in range(3,6):
            lst.append(board[i][j + 0])
            lst.append(board[i][j + 1])
            lst.append(board[i][j + 2])
        if not isValidSection(lst):
            return False
        lst = []
        j = 3
        for i in range(3,6):
            lst.append(board[i][j + 0])
            lst.append(board[i][j + 1])
            lst.append(board[i][j + 2])
        if not isValidSection(lst):
            return False
        lst = []
        j = 6
        for i in range(3,6):
            lst.append(board[i][j + 0])
            lst.append(board[i][j + 1])
            lst.append(board[i][j + 2])
        if not isValidSection(lst):
            return False
        lst = []
    
        j = 0
        for i in range(6,9):
            lst.append(board[i][j + 0])
            lst.append(board[i][j + 1])
            lst.append(board[i][j + 2])
        if not isValidSection(lst):
            return False
        lst = []
        j = 3
        for i in range(6,9):
            lst.append(board[i][j + 0])
            lst.append(board[i][j + 1])
            lst.append(board[i][j + 2])
        if not isValidSection(lst):
            return False
        lst = []
        j = 6
        for i in range(6,9):
            lst.append(board[i][j + 0])
            lst.append(board[i][j + 1])
            lst.append(board[i][j + 2])
        if not isValidSection(lst):
            return False

        return True
