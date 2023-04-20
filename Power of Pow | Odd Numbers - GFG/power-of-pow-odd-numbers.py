
class Solution:
	def sum_of_square_oddNumbers(self, n):
	    nums = 0
	    nums = n
	    start =1
	    sum = 0
		while(nums!=0):
		    sum = sum + start**2
		    start+=2
		    nums-=1

        return sum

#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.sum_of_square_oddNumbers(n)
		print(ans)
# } Driver Code Ends