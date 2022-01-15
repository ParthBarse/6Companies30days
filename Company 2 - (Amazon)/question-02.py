# Question 2 - Longest Mountain in Array


# Solution -

def longestMountain(a):

    i = 0
    j = -1
    k = -1
    p = 0
    d = 0
    n = 0

    if(len(a) < 3):
        return 0

    for i in range(len(a) - 1):
        if (a[i + 1] > a[i]):

            if (k != -1):

                k = -1
                j = -1

            if (j == -1):

                j = i

        else:

            if (a[i + 1] < a[i]):

                if (j != -1):
                    k = i + 1

                if (k != -1 and j != 1):
                    if (d < k - j + 1):
                        d = k - j + 1

            else:
                k = -1
                j = -1

    if(k != -1 and j != -1):
        if (d < k - j + 1):
            d = k - j + 1

    return d

if __name__ == "__main__":

    d = [1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5]

    print(longestMountain(d))





# Thanks in advance if anyone is reviewing this code.
# Program by - Parth Barse
# Suggest me anything about this code on email - (parthbarse72@gmail.com) or InstaId - (https://www.instagram.com/parth.barse)

# -------------------------------------------------------------------------------------
