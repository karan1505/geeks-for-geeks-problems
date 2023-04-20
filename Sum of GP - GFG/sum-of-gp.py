#User function Template for python3

class Solution:
	def sum_of_gp(self, n, a, r):
	    if(r==1):
	        return a*n
		return int((a*(1-r**n))/(1-r))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, a, r = input().split()
		n = int(n)
		a = int(a)
		r = int(r)
		ob = Solution();
		ans = ob.sum_of_gp(n, a, r)
		print(ans)
# } Driver Code Ends