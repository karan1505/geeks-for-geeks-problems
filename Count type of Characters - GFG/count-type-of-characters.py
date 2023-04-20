#User function Template for python3

class Solution:
    def count (self,s):
        uppercount = 0
        lowercount = 0
        numcount = 0
        specialcount = 0
        for i in s:
            if(i.isupper()):
                uppercount+=1
            elif(i.islower()):
                lowercount+=1
            elif(i.isdigit()):
                numcount +=1
            else:
                specialcount+=1
        
        arr = [0]*4
        arr[0] = uppercount
        arr[1] = lowercount
        arr[2] = numcount
        arr[3] = specialcount
        
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    res = ob.count (s)
    
    for i in res:
        print (i)
    
# Contributed By: Pranay Bansal

# } Driver Code Ends