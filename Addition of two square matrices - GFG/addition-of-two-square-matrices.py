#User function Template for python3

class Solution:
	def Addition(self, matrixA, matrixB):
	    i = 0
	    j = 0
		n = len(matrixA)
		for i in range(0,n):
		    for j in range(0,n):
		        matrixA[i][j] = matrixA[i][j] + matrixB[i][j]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrixA = []
		matrixB = []
		for _ in range(n):
			matrixA.append(list(map(int,input().split())))
		for _ in range(n):
			matrixB.append(list(map(int,input().split())))
		ob = Solution()
		ob.Addition(matrixA, matrixB)
		for i in range(n):
			for j in range(n):
				print(matrixA[i][j], end = " ")
			print()
# } Driver Code Ends