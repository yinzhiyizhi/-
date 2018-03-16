# 8. 旋转字符串

# 问题
# 给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)

# 样例
# 对于字符串 "abcdefg".
# offset=0 => "abcdefg"
# offset=1 => "gabcdef"
# offset=2 => "fgabcde"
# offset=3 => "efgabcd"

# 挑战 
# 在数组上原地旋转，使用O(1)的额外空间

offset=3
str="abcdefg"
result=[]
for n in range(-offset,len(str)-offset):
    result+=str[n]
print("".join(list(result)))

