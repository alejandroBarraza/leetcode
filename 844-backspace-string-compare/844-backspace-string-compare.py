class Solution: 
    def get_valid_index(self,string,index):
        count_backspaces = 0
        while index >=0:
            if string[index] == '#':
                count_backspaces+=1
            elif count_backspaces > 0:
                count_backspaces-=1
            else:
                break
            index-=1
        return index
             
    def backspaceCompare(self, s: str, t: str) -> bool:
        index1 = len(s) -1
        index2 = len(t) -1
        
        # loop over both str and compare s[index1] ==s[index2], if not same, return false. 
        # if we found a '#', skip over
        
        while (index1 >=0 or index2 >=0):
            # get valid index without '#'
            i1 = self.get_valid_index(s,index1)
            i2 = self.get_valid_index(t,index2)
            
            # 3 cases
            # both reach the end
            if (i1 < 0 and i2 < 0):
                return True
            # one reach the end
            if (i1 < 0 or i2 < 0):
                return False
            
            if s[i1] != t[i2]:
                return False
            
            index1 = i1 - 1
            index2 = i2 - 1
        return True
            
        

        