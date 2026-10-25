class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        result = []
        words1 = s1.split()
        words2 = s2.split()
        count = 0
        for word in words1:
            if word not in words2 and words1.count(word) == 1:
                result.append(word)
        for word in words2:
            if word not in words1 and words2.count(word) == 1:
                result.append(word)
        return result