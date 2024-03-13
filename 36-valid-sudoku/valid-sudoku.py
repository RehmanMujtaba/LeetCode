class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidSection(sec: List[str]) -> bool:
            hp = set()            
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
        
        for k in range(0, 9, 3):
            for j in range(0,9,3):
                lst = []
                for i in range(k,k+3):
                    lst.append(board[i][j + 0])
                    lst.append(board[i][j + 1])
                    lst.append(board[i][j + 2])
                if not isValidSection(lst):
                    return False

        return True
