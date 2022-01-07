# Question 3 - Given an array of positive numbers, the task is to find the number of possible contiguous subarrays having product less than a given number k.


# Solution -


def countSubarray(array, n, k):
    count = 0
    for i in range(0, n):

        # Counter for single element

        if array[i] < k:
            count += 1

        mul = array[i]

        for j in range(i + 1, n):

            # Multiply subarray
            mul = mul * array[j]

            # If this multiple is less than k, then increment
            if mul < k:
                count += 1
            else:
                break
    return count


array = [1, 2, 3, 4]
k = 10
size = len(array)
count = countSubarray(array, size, k)
print(count, end=" ")



# Thanks in advance if anyone is reviewing this code.
# Program by - Parth Barse
# Suggest me anything about this code on email - (parthbarse72@gmail.com) or Insta Id - (https://www.instagram.com/parth.barse)

# ----------------------------------------------------------------------------------------
