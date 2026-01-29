class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        while len(nums)>1:
            newNums=[0]*(len(nums)//2)
            n=len(nums)
        
        
            for i in range(n//2):
            
                if i%2==0:
                    newNums[i]=(min(nums[2*i], nums[2*i + 1]))

                elif i%2!=0:
                    newNums[i]=(max(nums[2 * i], nums[2 * i + 1]))

       

        
            nums=newNums
        return nums[0]


            
        