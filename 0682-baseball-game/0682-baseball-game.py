class Solution:
    def calPoints(self, operations: list[str]) -> int:
        result = []

        for i in range(len(operations)):
            if operations[i] not in ["+", "D", "C"]:
                result.append(int(operations[i]))

            elif operations[i] == "+":
                result.append(result[-1] + result[-2])

            elif operations[i] == "D":
                result.append(2 * result[-1])

            elif operations[i] == "C":
                result.pop()

        return sum(result)