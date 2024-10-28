class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minx = min(strs, key=len)
        
        prefix = strs[0]
        
        for string in strs:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:  #check for emptiness
                    return ""
        
        return prefix