#User function Template for python3

class Solution:
    def mulClock(self, num1, num2):
        val = num1*num2
        if(val<12):
            return val
        elif(val==0 or val==12):
            return 0
        else:
            return val%12


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        num1,num2=map(int,input().split())
        
        ob = Solution()
        print(ob.mulClock(num1,num2))
# } Driver Code Ends