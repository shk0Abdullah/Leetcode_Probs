class Solution:
    def isValid(self, s: str) -> bool:
        isValid = False
        dic = {
            "(":")",
            "[":"]",
            "{": "}"
        }
        stack = []
        for i in s:
            if i in "[{(":
                stack.append(i)
            elif i in dic.values() and stack and i == dic.get(stack[-1]):
                stack.pop()
                isValid = True
            else: 
                return False
        if len(stack) == 0 and len(s) != 0 and isValid:
            return True
        return False
