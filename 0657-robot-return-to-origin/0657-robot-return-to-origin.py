class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horizontal = 0
        vertical = 0

        for i in moves:
            if i == "R":
                horizontal += 1
            elif i == "L":
                horizontal -= 1
            elif i == "U":
                vertical += 1
            elif i == "D":
                vertical -= 1

        if horizontal == 0 and vertical == 0:
            return True
        else:
            return False