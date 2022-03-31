class Solution:
    def fourSum(self, arr: List[int], target: int) -> List[List[int]]:
        cuadruplets = []
        arr.sort()
        len_arr = len(arr)
        for i in range(len_arr -3):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            for j in range(i+1,len_arr -2 ):
                if j> i+1 and  arr[j] == arr[j-1]:
                    continue
                l,r = j + 1, len_arr - 1 
                while l < r:
                    f_sum = arr[i] + arr[j] + arr[l] + arr[r]
                    if f_sum < target:
                        l +=1
                    elif f_sum > target:
                        r-=1
                    else:
                        cuadruplets.append([arr[i],arr[j],arr[l],arr[r]])
                        l+=1
                        while l < r and arr[l] == arr[l-1]:
                            l+=1
        return cuadruplets
        