#User function Template for python3
import math
class Solution:
	def distance(self, x1, y1, x2, y2):
		sum = (x2-x1)**2 + (y2-y1)**2
        ans = sum**(0.5)
        if((ans-int(ans))>0.5):
            return math.ceil(ans)
        else:
            return math.floor(ans)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x1, y1, x2, y2 = input().split()
		x1 = int(x1);
		y1 = int(y1);
		x2 = int(x2);
		y2 = int(y2);
		ob = Solution();
		ans = ob.distance(x1, y1, x2, y2)
		print(ans)
# } Driver Code Ends