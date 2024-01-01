# -*- coding: utf-8 -*-
# edit by xty
# Leetcode 980


class Solution:
    def maxPath(self, grid: list[list[int]], x: int, y: int) -> int:
        if grid[y][x] == 2:
            for row in grid:
                try:
                    row.index(0)
                    return 0
                except ValueError:
                    pass
            return 1
        
        # 路径计数
        count = 0
        
        # 复制一份格子
        grid_new = [grid[i].copy() for i in range(len(grid))]
        # 起点已经走过，赋值为-1，方便判断
        grid_new[y][x] = -1
        
        # up
        if y - 1 >= 0 and grid[y-1][x] != -1:
            count += self.maxPath(grid_new, x, y-1)
        #down
        if y + 1 < len(grid) and grid[y+1][x] != -1:
            count += self.maxPath(grid_new, x, y+1)
        #left
        if x - 1 >= 0 and grid[y][x-1] != -1:
            count += self.maxPath(grid_new, x-1, y)
        #right
        if x + 1 < len(grid[0]) and grid[y][x+1] != -1:
            count += self.maxPath(grid_new, x+1, y)
        return count
        
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        # 找到起点坐标
        sidx, sidy = 0, 0
        for row in grid:
            try:
                sidx= row.index(1)
                break
            except ValueError:
                pass
            sidy += 1
        return self.maxPath(grid, sidx, sidy)
    
sul = Solution()
print(sul.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))

# a=[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# b=[a[x].copy() for x in range(len(a))]
# b[0][1]=45
# b[1][1]=22
# print(a, b)