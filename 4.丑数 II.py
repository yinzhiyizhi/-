# 4. 丑数 II

# 问题
# 设计一个算法，找出只含素因子2，3，5 的第 n 小的数。
# 符合条件的数如：1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

# 注意事项
# 我们可以认为1也是一个丑数

# 样例
# 如果n = 9， 返回 10

# 挑战 
# 要求时间复杂度为O(nlogn)或者O(n)

class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        list=[1]
        if n==1:
            return list[0]
            
        i2,i3,i5=0,0,0
        n_2,n_3,n_5=i2*2,i3*3,i5*5
        
        while len(list)<n:  
            while list[-1]>=n_2:
                n_2=list[i2]*2
                i2+=1
            while list[-1]>=n_3:
                n_3=list[i3]*3
                i3+=1
            while list[-1]>=n_5:
                n_5=list[i5]*5  
                i5+=1
            
            list.append(min(n_2,n_3,n_5))
        return list[-1]