#User function Template for python3

class Solution:
    def findElements(self,a, n):
        a.sort()
        b = [0]*(n-2)
        for i in range(0,n-2):
            b[i] = a[i]
        
        return b
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
    	n = int(input())
    	a = [int(x) for x in input().strip().split()]
    	ob=Solution()
    	print(*ob.findElements(a, n))
    	
    	T -= 1

if __name__ == "__main__":
    main()







# } Driver Code Ends