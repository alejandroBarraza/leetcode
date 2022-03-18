class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        arr_len = len(nums)
        
        for index,val in enumerate(nums):
            if index > 0 and val == nums[index - 1 ]:
                continue
            
            #two pointer sum with no repeat elements
            l, r = index + 1, arr_len -1
            while l < r:
                three_sum = val + nums[l] + nums[r]
                if three_sum > 0:
                    r-=1
                elif three_sum < 0:
                    l+=1
                else:
                    res.append([val,nums[l],nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return res
                    
        
#        t = o(nlogn) + o(n) + o(n^2) ===> O(n^2)
         # s = s(1) or s(n) if we count sort as s(n)
                    
            
                
            
            
        