class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        answer = []

        def pairs(current, open, close, n):
            if open == n and close == n:
                answer.append(current)
                return

            if open < n:
                pairs(current + "(", open + 1, close, n)

            if close < open:
                pairs(current + ")", open, close + 1, n)

        pairs("", 0, 0, n)

        return answer
