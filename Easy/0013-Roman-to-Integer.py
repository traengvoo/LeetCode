class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        romanToNum = {"I": 1, "V": 5, "X": 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for char in s:
            result+=romanToNum[char]
        for i in range(1,len(s)):
            if s[i-1]=="I" and (s[i]=="X" or s[i]=="V"):
                result-=2
            if s[i-1]=="X" and (s[i]=="L" or s[i]=="C"):
                result-=20
            if s[i-1]=="C" and (s[i]=="D" or s[i]=="M"):
                result-=200
        return result
