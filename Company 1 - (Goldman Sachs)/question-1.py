# Question 1 - Given an array of strings, return all groups of strings that are anagrams. The groups must be created in order of their appearance in the original array.


# *** Please run two solutions seperately for accurate output.

"""

***Solution 1 -

In this solution we will set words in list by default.

eg. - ["cat", "dog", "tac", "god", "act"]

"""


from collections import defaultdict


def groupAnagrams(words):
    groupedWords = defaultdict(list)

    for word in words:
        groupedWords["".join(sorted(word))].append(word)

    for group in groupedWords.values():
        print(" ".join(group))


if __name__ == "__main__":
    arr = ["cat", "dog", "tac", "god", "act"]
    groupAnagrams(arr)


# -------------------------------------------------------------------------------------


"""

***Solution 2 -

In this solution we will set words in list by user input (upto 5 words)

"""


def groupAnagrams(words):
    groupedWords = defaultdict(list)

    for word in words:
        groupedWords["".join(sorted(word))].append(word)

    for group in groupedWords.values():
        print(" ".join(group))


if __name__ == "__main__":
    arr = []

    for i in range(0, 5):
        words = input("Enter the Word - ")
        arr.append(words)

    groupAnagrams(arr)


# Thanks in advance if anyone is reviewing this code.
# Program by - Parth Barse
# Suggest me anything about this code on email - (parthbarse72@gmail.com) or Insta Id - (https://www.instagram.com/parth.barse)


# ------------------------------------------------------------------------------------------
