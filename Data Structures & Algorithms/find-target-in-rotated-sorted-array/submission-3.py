class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            m= l+ (r-l)//2 # srednji se refreshuje nakon svakog koraka dok ne postane target
            if target==nums[m]: #sredina je target
                return m
            
            if nums[l]<=nums[m]: #leva i preko pola je sortirana
                if target>nums[m] or target< nums[l]:
                    l=m+1 #nije u levom delu sortiranog ako je veca od srednjeg 
                    # a manja od levog
                    # znaci da pocinjemo od vecega broja a manji brojevi
                    # su shiftovani u desni deo


                else:
                    r=m-1 # u suprotnom jeste u levom delu
            else:
                if target< nums[m] or target > nums[r]:
                    r=m-1 #u levom je delu
                else:
                    l=m+1
        return -1
        
