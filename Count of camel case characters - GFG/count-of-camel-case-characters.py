#User function Template for python3

class Solution:
    def countCamelCase (self,s):
        count = 0
        for i in s:
            if(i.isupper()==1):
                count+=1
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print (ob.countCamelCase (s))

# Contributed By: Pranay Bansal

# } Driver Code Ends