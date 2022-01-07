# Question 4 - Given a string, Your task is to  complete the function encode that returns the run length encoded string for the given string.
# eg if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6″.


# Solution -


def encode(arr):

    n = len(arr)
    i = 0

    while i < n-1:
        count = 1

        while(i < n-1 and arr[i] == arr[i+1]):
            count += 1
            i += 1

        i += 1

        print(arr[i - 1] + str(count), end="")


if __name__ == "__main__":

    arr = "wwwwaaadexxxxxxywww"
    encode(arr)




# Thanks in advance if anyone is reviewing this code.
# Program by - Parth Barse
# Suggest me anything about this code on email - (parthbarse72@gmail.com) or Insta Id - (https://www.instagram.com/parth.barse)

# ----------------------------------------------------------------------------------------
