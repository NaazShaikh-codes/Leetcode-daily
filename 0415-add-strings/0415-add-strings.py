class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1) - 1
        n2 = len(num2) - 1
        carry = 0
        result = []

        while n1 >= 0 or n2 >= 0 or carry:

            digit1 = int(num1[n1]) if n1 >= 0 else 0
            digit2 = int(num2[n2]) if n2 >= 0 else 0

            total = digit1 + digit2 + carry

            result.append(str(total % 10))
            carry = total // 10

            n1 -= 1
            n2 -= 1

        return ''.join(result[::-1])


        