class Solution:
    def finalString(self, s: str) -> str:
        str = ""
        for i in s:
            if i=="i":
                str = str[: : -1]
            else:
                str += i
        return str

        