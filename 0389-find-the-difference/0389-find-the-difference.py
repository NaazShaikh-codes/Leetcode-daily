class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}
        for ch in s:
            count[ch] = count.get(ch,0) + 1  #ex. for alphabet "a" get the current count, if it is not there give 0, and then add 1
        for ch in t:
            if ch not in count or count[ch] == 0:
                return ch
            count[ch] -= 1
        