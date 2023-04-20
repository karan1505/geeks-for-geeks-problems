# Your task is to complete this function
# Function should return True/False or 1/0
def PalinArray(arr ,n):
    k = 0
    count = 0
    while(k!=n):
        use = arr[k]
        temp = str(use)
        if(temp[::1]==temp[::-1]):
            count+=1
        else:
            return 0
        k+=1
    
    if(count==n):
        return 1



#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends