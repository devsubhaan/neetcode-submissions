class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        l = len(board)

        for i in range(l):
            for val in board[i]:
                if not val in ["1","2","3","4","5","6","7","8","9","."]: #check if its valid num or empty
                    print("Length-1")
                    return False
            
            #check horizontal rows
            nrow = list(filter(lambda x: x != ".", board[i])) 
            if len(nrow) != len(set(nrow)):
                print("Length0")
                return False

            #check vertical rows
            tmp = set()
            for j in range(l):
                if board[j][i] == ".":
                    continue

                if board[j][i] in tmp:
                    print("Length")
                    return False

                tmp.add(board[j][i])

        #check each 3x3 grid
        for br in range(0,9,3):
            for bc in range(0,9,3):

                vals = set()

                for r in range(br,br+3):
                    for c in range(bc,bc+3):
                        if board[r][c] == ".":
                            continue

                        if board[r][c] in vals:
                            print("Length00")
                            return False

                        vals.add(board[r][c])

        return True
