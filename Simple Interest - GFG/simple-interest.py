#User function Template for python3

class Solution:
    def simpleInterest(self,A,B,C):
        int = T*(R/100)*P
        return int
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        P,R,T=map(int,input().strip().split(' '))
        ob=Solution()
        print('%.2f'%ob.simpleInterest(P,R,T))
# } Driver Code Ends