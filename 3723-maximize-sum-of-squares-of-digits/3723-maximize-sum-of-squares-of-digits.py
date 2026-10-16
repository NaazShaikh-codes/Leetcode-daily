class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        ans = []
        if sum > 9 * num:
            return ""
        while sum > 0 :
            digit = min(9, sum)
            ans.append(str(digit))
            sum -= digit
            num -= 1
        while num > 0:
            ans.append("0")
            num -= 1
        return "".join(ans)