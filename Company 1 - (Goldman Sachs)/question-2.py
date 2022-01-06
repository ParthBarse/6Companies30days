# Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y coordinates of two points: the left top corner and the right bottom corner of the rectangle. Two rectangles sharing a side are considered overlapping. (L1 and R1 are the extreme points of the first rectangle and L2 and R2 are the extreme points of the second rectangle).


# Solution -


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def doOverlap(l1, r1, l2, r2):

    if (l1.x == r1.x or l1.y == r1.y or l2.x == r2.x or l2.y == r2.y):
        return False

    if (l1.x >= r2.x or l2.x >= r1.x):
        return False

    if (r1.y >= l2.y or r2.y >= l1.y):
        return False

    return True


if __name__ == "__main__":
    l1 = Point(0, 10)
    r1 = Point(10, 0)
    l2 = Point(5, 5)
    r2 = Point(15, 0)

    if(doOverlap(l1, r1, l2, r2)):
        print("Rectangles Overlap")

    else:
        print("Rectangles Don't Overlap")



# Thanks in advance if anyone is reviewing this code.
# Program by - Parth Barse
# Suggest me anything about this code on email - (parthbarse72@gmail.com) or Insta Id - (https://www.instagram.com/parth.barse)

# ----------------------------------------------------------------------------------------
