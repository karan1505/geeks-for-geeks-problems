#User function Template for python3

def isVowel(char):
    vowels = "aeiouAEIOU"
    if char in vowels:
        return True
    else:
        return False

class Solution:
    def modify(self, s):
        Vowels = []
        for i in s:
            if(isVowel(i)==1):
                Vowels.append(i)
        
        ans = []
        count = 0
        Vowels[::1] = Vowels[::-1]
        for i in s:
            if(isVowel(i)==1):
                ans.append(Vowels[count])
                count+=1
            else:
                ans.append(i)
        
        rans = ''.join(ans)
        return rans
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.modify(s)
        print(ans)
# } Driver Code Ends