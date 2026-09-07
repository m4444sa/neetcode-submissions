class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in closeToOpen: #if c is closing
                if stack and stack[-1]==closeToOpen[c]: #if before it is the correct opening 
                    stack.pop() 
                else:
                    return False
            else: #if c is opening, i can add as many in stack
                stack.append(c)

        return True if not stack else False #if nothing is left, the parentheses are valid


