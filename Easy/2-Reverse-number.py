class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        a = abs(x)
        while a>0:
            result = result*10+(a%10)
            a=a//10
        if x<0:
            result = -result
            if result <= -2147483651:
                result = 0                
        if result>=2147483651:
            result = 0
        return result 
