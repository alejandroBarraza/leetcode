class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for x in range(len(nums)):
            y = target - nums[x] 
            if y in visited:
                return [x, visited[y]]
            else:
                visited[nums[x]] = x
           
        return None
            
    #     x + y = target
    #     y = target - x
        