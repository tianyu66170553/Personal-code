# -*- coding: utf-8 -*-
# edit by xty
# Leetcode 79

from collections import Counter

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        #剪枝1
        count=Counter(sum(board,[]))#Counter统计单列表中元素出现次数，用dic保存
        for char,num in Counter(word).items():
            if count[char]<num:
                return False
        m,n=len(board),len(board[0])
		#剪枝2，如果开头字母多于末尾字母，说明从后往前找更快
        c=0
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    c+=1
                elif board[i][j]==word[-1]:
                    c-=1
		
        if c>0:
            word = word[::-1]
        startPoints = []
        
        # 找到所有第一个字母的位置
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    startPoints.append([i, j])

        def findChar(i: int, boardStatus: int, r: int, c: int) -> bool:
            if i == len(word):
                return True
            
            for deltaR, deltaC in [[-1,0], [1,0], [0,-1], [0,1]]:
                nr, nc = r+deltaR, c+deltaC
                idx = nr*len(board[0])+nc
                if nr < 0 or nr >= len(board) or nc < 0 or nc >= len(board[0]):
                    continue
                if (boardStatus & 1<<idx) == 0 and board[nr][nc] == str(word[i]): 
                    if findChar(i+1, boardStatus | (1 << idx), nr, nc):
                        return True
            return False
                
        boardStatus = 0
        for point in startPoints:
            idx = point[0]*len(board[0])+point[1]
            if findChar(1, boardStatus|(1<<idx), point[0], point[1]):
                return True
            
        return False
    
solu = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(solu.exist(board, word))