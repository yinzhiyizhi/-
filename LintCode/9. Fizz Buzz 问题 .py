# 9. Fizz Buzz 问题

# 问题
# 给你一个整数n. 从 1 到 n 按照下面的规则打印每个数：
# 如果这个数被3整除，打印fizz.
# 如果这个数被5整除，打印buzz.
# 如果这个数能同时被3和5整除，打印fizz buzz.

# 样例
# 比如 n = 15, 返回一个字符串数组：
# [
#   "1", "2", "fizz",
#   "4", "buzz", "fizz",
#   "7", "8", "fizz",
#   "buzz", "11", "fizz",
#   "13", "14", "fizz buzz"
# ]

# 挑战 
# Can you do it with only one if statement?

class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        result=[]
        for i in range(1,n+1):
            if i%3==0 or i%5==0:
                if i%3==0 and i%5==0:
                    result.append("fizz buzz")
                    continue
                if i%3==0:
                    result.append("fizz")
                if i%5==0:
                    result.append("buzz")
            else:
                result.append("%d" % i)
        return result        

