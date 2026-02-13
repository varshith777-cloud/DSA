class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area=0
        n=len(height)
        L,R=0,len(height)-1

        while L<R:

            max_area=max(max_area,min(height[L],height[R])*(R-L))

            if height[L]<height[R]:
                L+=1
            else:
                R-=1

        return max_area

        

            

        