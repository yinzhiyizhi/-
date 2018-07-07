# 897. 海岛城市

# 问题
# Given a matrix of size n x m, the elements in the matrix are 0、1、2. 0 for the sea, 1 for the island, and 2 for the city on the island(You can assume that 2 is built on 1, ie 2 also represents the island).
# If two 1 are adjacent, then these two 1 belong to the same island. Find the number of islands with at least one city.

# 注意事项
# 我们只考虑上下左右为相邻。
# n <= 100，m <= 100。
# 你可以假设矩阵的四个边都被海包围。

# 样例
# Given mat =
# [
#      [1,1,0,0,0],
#      [0,1,0,0,1],
#      [0,0,0,1,1],
#      [0,0,0,0,0],
#      [0,0,0,0,1]
# ]
# , return 0.

# Explanation:
# There are 3 islands, but none of them contain cities.
# Given mat =
# [
#      [1,1,0,0,0],
#      [0,1,0,0,1],
#      [0,0,2,1,2],
#      [0,0,0,0,0],
#      [0,0,0,0,2]
# ]
# , return 2.

# Explanation:
# There are 3 islands, and two of them have cities.

class Solution:
    """
    @param grid: an integer matrix
    @return: an integer 
    """
    def numIslandCities(self, grid):
        # Write your code here
        count=0
        for n in range(0,len(grid)):
            for m in range(0,len(grid[0])):
                if grid[n][m]==2:
                    
                    count+=1
        return count            
