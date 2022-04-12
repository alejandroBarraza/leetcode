class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ptr_a = 0
        ptr_b = 0
        out = []
        while ptr_a < len(firstList) and ptr_b < len(secondList):
            lo = max(firstList[ptr_a][0],secondList[ptr_b][0])
            hi = min(firstList[ptr_a][1],secondList[ptr_b][1])
            
            if lo <= hi:
                out.append([lo,hi])
            
            if firstList[ptr_a][1] > secondList[ptr_b][1]:
                ptr_b+=1
            else:
                ptr_a+=1
        return out
                
                
        