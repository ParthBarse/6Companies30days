# Question 5 - Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included. Write a program to find Nth Ugly Number.


# Solution -


def maxDivide(a, b):
    while a % b == 0:
        a = a/b

    return a


def isUgly(no):

    no = maxDivide(no, 2)
    no = maxDivide(no, 3)
    no = maxDivide(no, 5)

    return 1 if no == 1 else 0


def getNthUglyNo(n):
    i = 1

    count = 1

    while n > count:
        i += 1
        if isUgly(i):
            count += 1

    return i


if __name__ == "__main__":

    n = int(input("Enter the nth Number - "))
    no = getNthUglyNo(n)
    print(str(n) + "th ugly no. is", no)




# Thanks in advance if anyone is reviewing this code.
# Program by - Parth Barse
# Suggest me anything about this code on email - (parthbarse72@gmail.com) or Insta Id - (https://www.instagram.com/parth.barse)

# ----------------------------------------------------------------------------------------
