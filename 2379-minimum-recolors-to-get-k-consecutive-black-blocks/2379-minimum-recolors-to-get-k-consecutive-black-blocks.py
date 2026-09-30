class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0
        for i in range(k):
            if blocks[i] == 'W':
                white += 1
        minimum = white
        for i in range(k, len(blocks)):
            # remove leftmost part
            if blocks[i - k] == 'W':
                white -= 1
            #add rightmost part
            if blocks[i] == 'W':
                white += 1
            minimum = min(minimum, white)
        return minimum