# Question 5 - For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).


# Solution -


class Solution(object):

    def gcdOfStrings(self, str1, str2):

        if len(str1) <= len(str2):
            temp = str1
        else:
            temp = str2


        n = len(temp)
        x = 1
        res = [""]

        while x <= n:
            if n%x == 0 and temp[:x] * (len(str1)//x) == str1 and temp[:x] * (len(str2)//x) == str2:
                res.append(temp[:x])

            x +=1

        return res[-1]


if __name__ == "__main__":

    ans = Solution()
    print(ans.gcdOfStrings("ABCABC", "ABC"))




# Thanks in advance if anyone is reviewing this code.
# Program by - Parth Barse
# Suggest me anything about this code on email - (parthbarse72@gmail.com) or Insta Id - (https://www.instagram.com/parth.barse)

# ----------------------------------------------------------------------------------------
