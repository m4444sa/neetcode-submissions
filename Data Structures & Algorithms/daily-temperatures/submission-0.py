class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # temp:index
        res= [0]* len(temperatures) #prazan stek

        for i, t in enumerate(temperatures):
            while stack and t> stack[-1][0]: # dok se stek ne isprazni ili dok trwnutna temperatura je toplija od one sa vrha steka
                stackT,stackI=stack.pop()
                res[stackI]=i-stackI
            stack.append((t,i))  

        return res