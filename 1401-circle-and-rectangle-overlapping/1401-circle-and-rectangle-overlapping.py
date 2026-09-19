class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int,
                     x1: int, y1: int, x2: int, y2: int) -> bool:

        sq_x_min = min(x1, x2)
        sq_x_max = max(x1, x2)
        sq_y_min = min(y1, y2)
        sq_y_max = max(y1, y2)

        closest_x = max(sq_x_min, min(xCenter, sq_x_max))
        closest_y = max(sq_y_min, min(yCenter, sq_y_max))

        distance_x = xCenter - closest_x
        distance_y = yCenter - closest_y

        final_distance = (distance_x ** 2) + (distance_y ** 2)

        return final_distance <= (radius ** 2)