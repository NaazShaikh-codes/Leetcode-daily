class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        result =[]
        for ch in s:
            if ch==y:
                result.append(ch)
        for ch in s:
            if ch!=x and ch!=y:
                result.append(ch)
        for ch in s:
            if ch==x:
                result.append(ch)
        return "".join(result)
        


 