#User function Template for python3

class Solution:
    def isDigitSumPalindrome(self,N):
        numstr = str(N)
        sum = 0
        temp = 0
        for i in range(0,len(numstr)):
            temp = int(numstr[i])
            sum = sum + temp

        sumstr = str(sum)
        if(sumstr[::1]==sumstr[::-1]):
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
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends