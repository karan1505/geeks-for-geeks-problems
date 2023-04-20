#User function Template for python3

class Solution:
    def printFloydTriangle(self, N):
        var = 1
        num = 1
    	while(var!=N+1):
    	    for i in range(0,var):
    	        print(num,end=" ")
    	        num = num+1
    	    var+=1
    	    print("")


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printFloydTriangle(N)
        
# } Driver Code Ends