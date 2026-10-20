class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        def backtrack(start, result, total):
            for i in range(start, len(candidates)):
                if total + candidates[i] > target:
                    continue
                if total + candidates[i] == target:
                    output.append(result + [candidates[i]])
                elif total + candidates[i] < target:
                    result.append(candidates[i])
                    backtrack(i, result, total + candidates[i])
                    result.pop()
        backtrack (0, [], 0)
        return output