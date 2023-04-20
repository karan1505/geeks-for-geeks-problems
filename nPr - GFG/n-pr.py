#User function Template for python3

class Solution:
    def nPr(self, n, r):
        def fact(k):
            if(k==0):
                return 1
            return k*fact(k-1)
        ans = fact(n)/fact(n-r)
        
        return int(ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nPr(n, r))
# } Driver Code Ends