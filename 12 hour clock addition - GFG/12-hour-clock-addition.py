#User function Template for python3

class Solution:
    def clockSum(self, num1, num2):
        sum = num1 + num2
        if(sum<12):
            return sum
        elif(sum==12):
            return 0
        else:
            return sum%12

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        num1, num2 = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.clockSum(num1, num2))

# } Driver Code Ends