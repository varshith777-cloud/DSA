class Solution:
    def check(self, nums: List[int]) -> bool:

        sorted_arr=sorted(nums)
        i=0
        while i<len(nums):
            ele=nums.pop()
            nums.insert(0,ele)   
            i+=1
            if nums==sorted_arr:
                return True

        return False

            