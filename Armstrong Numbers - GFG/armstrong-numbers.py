#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (ob, n):
        dig1 = int(n/100)
        dig2 = int(n/10) - 10*dig1
        dig3 = n - 100*dig1 - 10*dig2
        if((dig1*dig1*dig1 + dig2*dig2*dig2 + dig3*dig3*dig3)==n):
            return "Yes"
        else:
            return "No"
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends