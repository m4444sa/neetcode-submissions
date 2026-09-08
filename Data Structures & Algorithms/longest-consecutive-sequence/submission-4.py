class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:    
        longest=0
      
        
        kurac=set(nums)
        for k in kurac:
            if (k-1) not in kurac:
                leng=1
                curr=k
                while curr+1 in kurac:
                    curr+=1
                    leng+=1

                longest=max(leng,longest)

        return longest


                
            
        
               
        




        