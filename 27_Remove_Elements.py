class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Keep doing this while the value is in the list, 
        # whenever it happens remove that value 
        # from the list 
        # The question is not very clear: it wants you to remove the item from the original
        # list, not creating a new one.
        while val in nums:
            nums.remove(val)


        
