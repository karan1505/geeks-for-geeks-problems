#User function Template for python3

class Solution:
    def sumOfDigits (self, N):
        numstr = str(N)
        digits = len(numstr)
        sum = 0
        for i in range(0,digits):
            tempnumstr = numstr[i]
            tempnum = int(tempnumstr)
            sum = sum + tempnum
        
        return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.sumOfDigits(N))
# } Driver Code Ends