from itertools import combinations 
  
def findQuadruplets(lst, key): 
      
    def valid(val): 
        return sum(val) == key 
          
    return list(filter(valid, list(combinations(lst, 4)))) 
  
# Driver Code 

lst = [int(x) for x in input('Inpute1:').split()]

print('Output1:',findQuadruplets(lst, 2)) 
