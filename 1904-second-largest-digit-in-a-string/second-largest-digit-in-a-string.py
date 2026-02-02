class Solution:
    def secondHighest(self, s: str) -> int:
        highest=sec_high=-1

        for char in s:
            if char.isdigit():
                digit=int(char)
            
                if digit>highest:
                    highest,sec_high=digit,highest
                elif sec_high<digit<highest:
                    sec_high=digit
            

        return sec_high

      
     

                


        