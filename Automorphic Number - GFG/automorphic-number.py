#User function Template for python3

class Solution:
	def is_AutomorphicNumber(self, n):
		sq = n**2
		numstr = str(n)
		sqnumstr = str(sq)
		revnum = numstr[::-1]
		revsqnum = sqnumstr[::-1]
		
		for i in range(0,len(revnum)):
		    if(revnum[i]==revsqnum[i]):
		        continue
		    else:
		        return "Not Automorphic"
        
        return "Automorphic"


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_AutomorphicNumber(n)
		print(ans)
# } Driver Code Ends