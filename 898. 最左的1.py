# 898. 最左的1

# 问题
# 一个二维数组，每一行都只有0和1，前面部分是0，后一部分是1，找到数组里面所有行中最左边的1所在的列数。

# 注意事项
# 数组的行数，列数不超过1000
# 为了约束时间复杂度，你的程序将会运行50000次

# 样例
# 给出 arr = [[0,0,0,1],[1,1,1,1]], 返回 0。
# 解释：
# arr[1][0]为所有行中最左边的1，其所在的列为0。

# 给出 arr = [[0,0,0,1],[0,1,1,1]], 返回 1。
# 解释：
# arr[1][1]为所有行中最左边的1，其所在的列为1。

class Solution:
    """
    @param arr: The 2-dimension array
    @return: Return the column the leftmost one is located
    """
    def getColumn(self, arr):
        # Write your code here
        n=0
        for i in range(0,1001):
            if arr[0][i]==1 or arr[1][i]==1:
                n=i
                break
        return n    
