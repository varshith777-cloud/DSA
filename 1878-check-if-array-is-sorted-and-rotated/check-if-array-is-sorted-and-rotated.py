class Solution:
    def check(self, nums: List[int]) -> bool:

        sorted_arr=sorted(nums)

        for i in range(len(nums)):
            ele=nums.pop()
            nums.insert(0,ele)    
            if nums==sorted_arr:
                return True

        return False

            