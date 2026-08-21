class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
          return False 
        hash_map ={} 
        for char in s:
         hash_map[char] = hash_map.get(char,0)+1
        for char in t:
         hash_map[char] = hash_map.get(char,0)-1
 
        for values in hash_map.values():
          if values !=0:
            return False

        return True

    