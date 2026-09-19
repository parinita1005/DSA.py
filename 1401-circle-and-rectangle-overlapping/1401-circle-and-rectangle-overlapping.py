class Solution:
    def checkOverlap(self, r, cx, cy, x1, y1, x2, y2) -> bool:
        
        closest_x = max(x1, min(cx, x2))
        closest_y = max(y1, min(cy, y2))

        distance_squared = (cx - closest_x)**2 + (cy - closest_y)**2

        if distance_squared <= r**2:
            return True
        else:
            return False