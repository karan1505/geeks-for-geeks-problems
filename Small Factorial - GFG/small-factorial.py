#User function Template for python3

class Solution:
	def find_fact(self, n):
		def fact(x):
		    if(x==0):
		        return 1 
		    return x*fact(x-1)
		return fact(n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.find_fact(n)
		print(ans)

# } Driver Code Ends