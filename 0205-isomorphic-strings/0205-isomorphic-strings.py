class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        #if lengths not matching its false
        if len(s) != len(t):
            return False
        
        mp = {}
        used_values = set()


        for i in range(len(s)):
            
            #if s's letter in map
            if s[i] in mp:

                #but it does not correspond to mapped value (means its duplicate)
                if mp[s[i]] != t[i]:
                    return False

            #if its first time we see s[i]
            else:

                #did we use t[i] already to map?
                if t[i] in used_values:
                    return False
                
                #if not, map onto it
                mp[s[i]] = t[i]

                #add unique values of t for further check
                used_values.add(t[i])
        
        return True

