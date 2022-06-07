class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # a + b = target
        # target - a = b
        # i need to find b , for find b in the arr i will save the values
        # i already see in a dic
        # dic = {
        #     value: position
        # }
        
        seen ={}
        for i in range(len(nums)):
            if target - nums[i] not in seen:
                seen[nums[i]] = i  
            else:
                return [ i , seen[target - nums[i]] ]
        return False

                
        
        
        
        