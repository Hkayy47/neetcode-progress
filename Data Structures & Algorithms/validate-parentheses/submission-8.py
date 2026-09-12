class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {'(', '{', '['}
        closing = {')', ']', '}'}
        for c in s:
            if c in opening:
                stack.append(c)
            if c in closing:
                if not stack:
                    return False
                prev = stack.pop()
                flag = False
                if c == ')' and prev == '(':
                    flag = True
                elif  c == '}' and prev == '{' :
                    flag = True
                elif c == ']' and prev == '[' :
                    flag = True
                if not flag :
                    return False

                
        if len(stack) == 0 :
            return True
        else: 
            return False


