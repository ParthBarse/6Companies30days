# Function to convert a given number to an Excel column
def getColumnName(n):
 
    # initialize output string as empty
    result = ''
 
    while n > 0:
 
        # find the index of the next letter and concatenate the letter
        # to the solution
 
        # here index 0 corresponds to `A`, and 25 corresponds to `Z`
        index = (n - 1) % 26
        result += chr(index + ord('A'))
        n = (n - 1) // 26
 
    return result[::-1]
 
 
if __name__ == '__main__':

    r = 13
    print(getColumnName(r))