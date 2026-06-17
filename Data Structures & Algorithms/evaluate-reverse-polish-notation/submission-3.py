class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                valueOne = stack.pop()
                valueTwo = stack.pop()
                
                if tokens[i] == "+":
                    Sum = int(valueOne) + int(valueTwo)
                    stack.append(str(Sum))
                  
                elif tokens[i] == "-":
                    dif = int(valueTwo) - int(valueOne)
                    stack.append(str(dif))
                 
                elif tokens[i] == "*":
                    prod = int(valueOne) * int(valueTwo)
                    stack.append(str(prod))
                   
                elif tokens[i] == "/":
                    quo = int(int(valueTwo) / int(valueOne))
                    stack.append(str(quo))
                
        return int(stack[-1])
