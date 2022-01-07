# Question 7 - Distributing M items in a circle of size N starting from K-th position


# Solution -


def numDecodings(s: str) -> int:
    if len(s) == 0 or (len(s) == 1 and s[0] == '0'):
        return 0

    return numDecodingHelper(s, len(s))


def numDecodingHelper(s: str, n: int):
    if n == 0 or n == 1:
        return 1

    count = 0
    if s[n - 1] > "0":
        count = numDecodingHelper(s, n-1)

    if (s[n - 2] == "1" or (s[n - 2] == "2" and s[n - 1] < "7")):

        count += numDecodingHelper(s, n-2)
    return count


if __name__ == "__main__":

    digits = "1234"
    print("Count is ", numDecodings(digits))



# Thanks in advance if anyone is reviewing this code.
# Program by - Parth Barse
# Suggest me anything about this code on email - (parthbarse72@gmail.com) or InstaId - (https://www.instagram.com/parth.barse)

#-------------------------------------------------------------------------------------
