class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = 0
        consonants = 0
        vowel_str = "aeiouAEIOU"
        for i in word:
            if i.isalpha():
                if i in vowel_str:
                    vowels += 1
                else:
                    consonants += 1
            elif not i.isdigit():
                return False
        return vowels >= 1 and consonants >= 1
