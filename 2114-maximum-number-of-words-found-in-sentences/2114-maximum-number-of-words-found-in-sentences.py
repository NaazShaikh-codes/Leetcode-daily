class Solution(object):
    def mostWordsFound(self, sentences):
        max_count = 0
        for sentence in sentences:
            words = sentence.split()
            count = 0
            for word in words:
                count += 1
            if count > max_count:
                max_count = count
        return max_count