class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        
        result = set()

        for i in range(len(digits)):
            if digits[i] == 0:
                continue

            for j in range(len(digits)):
                if i == j:
                    continue

                for k in range(len(digits)):
                    if i == k or j == k:
                        continue

                    if digits[k] % 2 == 0:
                        number = (digits[i] * 100) + (digits[j] * 10) + digits[k]
                        result.add(number)

        return len(result)