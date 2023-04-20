#User function Template for python3
import math
class Solution:
	def findFocalLength(self, R, type):
		if(type=="concave"):
		    return math.floor(R/2)
		else:
		    return math.floor(-R/2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		type = input()
		R = float(input())
		ob = Solution()
		ans = ob.findFocalLength(R, type)
		print(ans)
# } Driver Code Ends