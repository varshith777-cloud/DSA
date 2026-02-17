class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        clen=bestl=1
        n=len(arr)
        if n==0: return 0
        if n==1: return 1
        clen=2 if arr[1]!=arr[0] else 1
        bestl=clen
        i=2
        while(i<len(arr)):
            if arr[i]==arr[i-1]:
                clen=1
            elif (arr[i]-arr[i-1])*(arr[i-1]-arr[i-2])<0:
                clen+=1
            else:
                clen=2
            bestl=max(bestl,clen)
            i+=1
        return bestl






       