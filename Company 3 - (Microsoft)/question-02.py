"""
class Solution:
    def isPossible(self,N,prerequisites):
        waits = {i: [] for i in range(N)}
        blocks = {i:[] for i in range(N)}
        
        for first, second in prerequisites:
            waits[first].append(second)
            blocks[second].append(first)
            
        ready = [i for i in range(N) if not waits[i]]
        done = set()
        while ready:
            current = ready.pop(0)
            done.add(current)
            for dependent in blocks[current]:
                waits[dependent].remove(current)
                if not waits[dependent]:
                    ready.append(dependent)
        
        return len(done) == N
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends
"""