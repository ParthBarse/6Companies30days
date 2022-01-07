# Question 11 - Find the repeating and the missing


# Solution -


def printTwoElements(arr, size):
    for i in range(size):
        if arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]

        else:
            print("The repeating element is ", abs(arr[i]))

    for i in range(size):
        if arr[i] > 0:
            print("and the missing element is ", i+1)


if __name__ == "__main__":

    arr = [7, 3, 4, 5, 5, 6, 2]
    n = len(arr)
    printTwoElements(arr, n)



# Thanks in advance if anyone is reviewing this code.
# Program by - Parth Barse
# Suggest me anything about this code on email - (parthbarse72@gmail.com) or InstaId - (https://www.instagram.com/parth.barse)

#-------------------------------------------------------------------------------------
