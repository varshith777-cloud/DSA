class Solution:
    def reverseWords(self, s: str) -> str:

        words=s.split()
        count=0
        res=""

        for i in words:

            if count==0:
                res=i+res
                count+=1

            else:
                res=i+" "+res

        return res



       

       
       

        