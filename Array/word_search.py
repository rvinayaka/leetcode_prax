
def word_search(board, word):
    rows = len(board)
    cols = len(board[0])
    path = set()

    def dfs(r, c, i):
        if i == len(word):      #$ last char of searching word
            return True
        
        if (r < 0 or c < 0 or               #! not existing i.e less than 0
            r >= rows or c >= cols or       #! not existing i.e greater than len(board)
            word[i] != board[r][c] or       #! word not in board
            (r, c) in path):                #! visiting the same position again
            return False
        
        path.add((r, c))          #? add the found char position to the path 
        
        #$ searching the adjacent positions (i.e top, right, bottom, left)
        res = (dfs(r + 1, c, i + 1) or      #? right
            dfs(r - 1, c, i + 1) or      #? left
            dfs(r, c + 1, i + 1) or      #? top
            dfs(r, c - 1, i + 1))        #? bottom
        
        path.remove((r, c))       #? remove postion bcoz we no longer visiting the positon
        return res


    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

arr = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word2 = "ABCB"

print(word_search(board, word))         #* True
print(word_search(arr, word2))          #* False