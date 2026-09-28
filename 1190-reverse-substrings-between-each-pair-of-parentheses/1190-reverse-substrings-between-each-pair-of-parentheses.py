class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        i = 0
        while i < len(s):
            if s[i] == "(":
                stack.append("")
            elif s[i] == ")":
                word = stack.pop()
                word = word[::-1]
                stack[-1] += word  # remove, reverse, add
            else:
                stack[-1] += s[i]
            i += 1
        return stack[0]
