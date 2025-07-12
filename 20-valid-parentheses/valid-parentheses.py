class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        dict = {'(':')','{':'}','[':']'}
        stack = []
        for i in s:
            if i in dict.keys():
                stack.append(i)
            else:
                if stack == []:
                    return False
                last_ele = stack.pop()
                if i != dict[last_ele]:
                    return False
        return stack == []