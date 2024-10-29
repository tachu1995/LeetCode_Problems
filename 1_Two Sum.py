class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = {}
        for i, value in enumerate(nums):
            result = target - value
            if result in answer:
                return(answer[result],i)
            answer[value]=i
        return 
        
