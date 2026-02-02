class Solution:
    def secondHighest(self, s: str) -> int:
        digits=set()

        for char in s:
            if char.isdigit():
                digit=int(char)
                digits.add(digit)

        if len(digits)<2:
            return -1
        
        digits=sorted(digits)
        return digits[-2]
        


        