import math


class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.area = .5 * self.a * self.b

    def is_right(self):
        angle1 = math.degrees(math.asin(self.a/self.c))
        angle2 = math.degrees(math.asin(self.b/self.c))
        angle = round(angle1 + angle2)
        if angle == 90:
            return True
        return False


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
triangle = RightTriangle(input_c, input_a, input_b)
if triangle.is_right():
    print(triangle.area)
else:
    print("Not right")
