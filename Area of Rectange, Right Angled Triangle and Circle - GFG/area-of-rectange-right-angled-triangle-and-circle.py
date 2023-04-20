#User function Template for python3

class Solution:
    def getAreas(self, L , W , B , H , R):
        rectarea = L*W
        triarea = 0.5*B*H
        circarea = 3.14*R*R
        areas = [0]*3
        areas[0] = int(rectarea)
        areas[1] = int(triarea)
        areas[2] = int(circarea)
        return areas


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        L,W,B,H,R=map(int,input().split())
        
        ob = Solution()
        ptr = ob.getAreas(L,W,B,H,R)
        
        print(ptr[0],ptr[1],ptr[2])
# } Driver Code Ends