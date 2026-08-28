class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            else:
                if not stack:
                    return False

                if stack.pop() != char:
                    return False
                
                

        
        if not stack:
            return True
        
        return False