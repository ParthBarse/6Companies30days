# Question 7 - Distributing M items in a circle of size N starting from K-th position


# Solution -


def lastPosition(n, m, k):
    if(m <= n-k+1):
        return m+k-1

    m = m-(n-k+1)

    if(m % n == 0):
        return 0
    else:
        return m % n


if __name__ == "__main__":

    n = 5
    m = 8
    k = 2
    print(lastPosition(n, m, k))
    
    

    # Thanks in advance if anyone is reviewing this code.
    # Program by - Parth Barse
    # Suggest me anything about this code on email - (parthbarse72@gmail.com) or Insta Id - (https://www.instagram.com/parth.barse)

    # ----------------------------------------------------------------------------------------
