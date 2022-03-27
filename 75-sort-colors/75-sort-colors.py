class Solution:
    def swap(self,arr,left,right):
        arr[left],arr[right] = arr[right], arr[left]
        
    def sortColors(self, arr: List[int]) -> None:
        l, r = 0, len(arr) -1
        i = 0
        
        while i <= r:
            # case 1 ) arr[i] is 0 :
            if arr[i] == 0:
                self.swap(arr,i,l)
                l+=1
                i+=1
            
            elif arr[i] == 1:
                i+=1
            else:
                self.swap(arr,i,r)
                r-=1
            
                
            
            
                
        
        