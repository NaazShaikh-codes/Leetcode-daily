class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge_map = {}
        
        for item in knowledge:
            knowledge_map[item[0]] = item[1]
        ans = ""
        i = 0
        while i < len(s):
            if s[i] != "(":
                ans += s[i]
                i += 1
            else:
                j = i + 1
                key = ""             
                while s[j] != ")":
                    key += s[j]
                    j += 1           
                if key in knowledge_map:
                    ans += knowledge_map[key]
                else:
                    ans += "?"               
                i = j + 1
        return ans