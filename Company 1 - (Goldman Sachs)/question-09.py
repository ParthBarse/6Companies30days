# Question 9 - Given a pattern containing only I's and D's. I for increasing and D for decreasing.


# Solution -


def printMinNumberForPattern(arr):
    curr_max = 0
    last_entry = 0
    i = 0
    lnarr = len(arr)

    while i < lnarr:

        noOfNextD = 0

        if arr[i] == "I":

            j = i + 1

            while j < lnarr and arr[j] == "D":
                noOfNextD += 1
                j += 1

            if i == 0:
                curr_max = noOfNextD + 2
                last_entry += 1

                print("", last_entry, end="")
                print("", curr_max, end="")

                last_entry = curr_max

            else:

                curr_max += noOfNextD + 1
                last_entry = curr_max
                print("", last_entry, end="")

            for k in range(noOfNextD):
                last_entry -= 1
                print("", last_entry, end="")
                i += 1
        
        elif arr[i] == "D":
            if i == 0:
                j = i + 1
                while j < lnarr and arr[j] == "D":
                    noOfNextD +=1
                    j += 1

                curr_max = noOfNextD + 2
                print("", curr_max, curr_max - 1, end="")
                last_entry = curr_max - 1

            else:
                print("", last_entry - 1, end="")
                last_entry -= 1

        i += 1
    print()




if __name__ == "__main__":
    printMinNumberForPattern("IDID")
    printMinNumberForPattern("I")



# Thanks in advance if anyone is reviewing this code.
# Program by - Parth Barse
# Suggest me anything about this code on email - (parthbarse72@gmail.com) or InstaId - (https://www.instagram.com/parth.barse)

#-------------------------------------------------------------------------------------
