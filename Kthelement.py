class Solution:
    def findKthPositive(self, arr,k) -> int:
        if not arr:
            return 1
        if k>arr[-1]:
            return k+len(arr)    
        i=1
        arr=set(arr)
        cur=-1
        while i<=3000 and k>0:
            if i in arr:
                i+=1
            else:
                cur=i
                i+=1
                k-=1
        return cur
val=Solution()
n,k=map(int,input().split())
nums=list(map(int,input().split()))
print(val.findKthPositive(nums,k))
