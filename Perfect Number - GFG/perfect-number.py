#User function Template for python3

class Solution:
    def isPerfect(self,N):
        def fact(x):
            if(x==0):
                return 1
            else:
                return x*fact(x-1)
        numstr = str(N)
        sum = 0
        for i in range(0,len(numstr)):
            digi = int(numstr[i])
            sum = sum + fact(digi)
        if(sum==N):
            return 1
        else:
            return 0
            
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isPerfect(N))   
# } Driver Code Ends