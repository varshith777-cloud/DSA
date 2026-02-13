class Solution:
    def trap(self, height: List[int]) -> int:

        
        water=0
        left,right=0,len(height)-1
        left_max,right_max=height[left],height[right]
        
        while left<right:
            if left_max<right_max:
                left+=1
                curr_bar=height[left]
                if curr_bar>left_max:
                    left_max=curr_bar
                water+=left_max-curr_bar
            else:
                right-=1
                curr_bar=height[right]
                if curr_bar>right_max:
                    right_max=curr_bar
                water+=right_max-curr_bar

        return water

        