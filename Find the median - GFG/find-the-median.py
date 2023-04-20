#User function Template for python3
import math
class Solution:
	def find_median(self, v):
		v.sort()
		length = len(v)
		if(length%2==0):
		    p = int(length/2)
		    mid = v[p] + v[p-1]
		    mid = mid/2
		    return int(mid)
		else:
		    return v[int(length/2)]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends