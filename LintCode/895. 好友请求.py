# 895. 好友请求

# 问题
# 给定一个长为n的数组Ages, 其中第i个元素表示第i个人的年龄。求这个n个人，发送的好友请求的总数。其中，
# 1. 如果Age(B) <= (1/2)Age(A) + 7, A不会给B发请求
# 2. 如果Age(B) > Age(A)， A不会给B发请求
# 3. 如果Age(B) < 100 and Age(A) > 100, A不会给B发请求
# 4. 不满足1，2，3，则A会给B发请求。

# 注意事项
# Ages.length <= 1000。
# 每个人的年龄大于0，小于150。

# 样例
# 给出Ages = [10,39,50], 返回 1。
# 解释：
# 只有年龄为50的人会给年龄为39的人发送好友请求。

# 给出Ages = [101,79,102], 返回 1。
# 解释：
# 只有年龄为102的人会给年龄为101的人发送好友请求。

class Solution:
    """
    @param ages: The ages
    @return: The answer
    """
    def friendRequest(self, ages):
        # Write your code here
        count=0
        for A in range(len(ages)):
            for B in range(len(ages)):
                if A==B or ages[B]>ages[A]:
                    continue
                elif ages[B]<=((1/2)*ages[A]+7):
                    continue
                elif ages[B]<100 and ages[A]>100:
                    continue
                else:
                    count+=1
        return count             
