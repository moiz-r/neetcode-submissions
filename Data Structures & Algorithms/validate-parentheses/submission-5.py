class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = []
        if s[0] not in ["(", "{", "["]:
            return False
        for idx, b in enumerate(s):
            if b in ["(", "{", "["]:
                stack.append(b)
            else:
                if stack:
                    out = stack.pop()
                    if out == '(' and b == ')' or out == '{' and b == '}' or out == '[' and b == ']':
                        continue
                    else:
                        return False
                else:
                    return False
            
        if len(stack) > 0:
            return False
        
        return True