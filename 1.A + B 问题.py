# 1. A + B 问题

# 问题：
# 给出两个整数a和b, 求他们的和, 但不能使用 + 等数学运算符。

# 注意事项
# 你不需要从输入流读入数据，只需要根据aplusb的两个参数a和b，计算他们的和并返回就行。

# 说明
# a和b都是 32位 整数么？
# 是的
# 我可以使用位运算符么？
# 当然可以

# 样例
# 如果 a=1 并且 b=2，返回3

# 挑战 
# 显然你可以直接 return a + b，但是你是否可以挑战一下不这样做？

class Solution:
    """
    @param: a: An integer
    @param: b: An integer
    @return: The sum of a and b
    """
    def aplusb(self,a, b):
        # write your code here
        
        sum=0
        carry=0
        for i in range(32):
            val=0
            a1=a&1
            b1=b&1
            if a1==0 and b1==0 and carry==0:
                val=0
                carry=0
            elif a1==1 and b1==1 and carry==1:
                val=1
                carry=1
            elif (a1==0 and b1==0) or (a1==0 and carry==0) or (b1==0 and carry==0):
                val=1
                carry=0
            else:
                val=0
                carry=1
            val=val<<i
            sum=sum|val
            a=a>>1
            b=b>>1
        return sum