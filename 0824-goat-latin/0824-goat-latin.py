class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        vowels = ['a', 'e', 'i', 'o', 'u']
        result = []
        for i, word in enumerate(sentence):
            if word[0].lower() in vowels:
                word = word + "ma"
            else:
                word = word[1:] + word[0] + "ma"
            word += "a" * (i + 1)
            result.append(word)
        return " ".join(result)