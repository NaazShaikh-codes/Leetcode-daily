class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(0)
            else:
                A = stack.pop()
                if A == 0:
                    A = 1
                else:
                    A = 2 * A
                stack[-1] += A
        return stack[0]
