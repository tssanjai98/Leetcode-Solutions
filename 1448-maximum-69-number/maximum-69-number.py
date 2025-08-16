class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))     
        maxx = num
        for i in range(len(s)):
            temp = s[:]       
            if temp[i] == '6':
                temp[i] = '9'
            else:
                temp[i] = '6'
            maxx = max(maxx, int("".join(temp)))
        return maxx