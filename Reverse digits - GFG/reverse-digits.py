#User function Template for python3

class Solution:
	def reverse_digit(self, n):
		numb = str(n)
		rev = numb[::-1]
		rev=list(rev)
		i=0
		while(1):
		    if(rev[i]=="0"):
		        del rev[i]
		    else:
		        break
		
		
		ans = ''.join(rev)
		return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
# } Driver Code Ends