class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(b + a)
            elif i == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif i == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(b * a)
            elif i == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(i))
        return stack[0]