# 6. 合并排序数组 II

# 问题
# 合并两个排序的整数数组A和B变成一个新的数组。

# 样例
# 给出A=[1,2,3,4]，B=[2,4,5,6]，返回 [1,2,2,3,4,4,5,6]

# 挑战 
# 你能否优化你的算法，如果其中一个数组很大而另一个数组很小？

class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        C=A+B
        C.sort()
        return C