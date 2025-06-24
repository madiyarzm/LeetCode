class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        mp = {}
        used_values = set()


        for i in range(len(s)):
            
            if s[i] in mp:

                if mp[s[i]] != t[i]:
                    return False

            else:
                if t[i] in used_values:
                    return False
                
                mp[s[i]] = t[i]
                used_values.add(t[i])
        
        return True

