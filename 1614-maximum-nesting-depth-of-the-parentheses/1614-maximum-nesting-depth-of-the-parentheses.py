class Solution:
    def maxDepth(self, s: str) -> int:
        max_length = 0
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
            elif i ==")":
                stack.pop()
            if len(stack) > max_length:
                max_length = len(stack)
        return max_length
        