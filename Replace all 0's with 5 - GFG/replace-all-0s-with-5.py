#function should return an integer
#your task is to compplete this function

def list_to_num(num_list):
    num_str = ''.join(map(str, num_list))
    return int(num_str)
    
class Solution:
    def convertFive(self,n):
        num = str(n)
        changednum = [0]*len(num)
        for i in range(0,len(num)):
            if(num[i]!="0"):
                changednum[i]=num[i]
            else:
                changednum[i]="5"
        ans = list_to_num(changednum)
            
        return ans

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        print(Solution().convertFive(n))
# Contributed by: Harshit sidhwa

# } Driver Code Ends