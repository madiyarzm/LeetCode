class Solution:
    def minMaxDifference(self, num: int) -> int:
        lst = list(str(num))
        mx_val = 0
        mn_val = float('inf')

        j = 0

        while j < len(lst):
            
            i = 0
            first = lst[j]
            mx = []

            while i < len(lst):
                
                if first == lst[i]:
                    mx.append('9')
                
                else:
                    mx.append(lst[i])
                
                i += 1
            
            #print(int(''.join(mx)), " this is mx")
            mx_val = max(mx_val, int(''.join(mx)))
            
            i = 0
            mn = []
            
            while i < len(lst):
                
                if first == lst[i]:
                    mn.append('0')
                
                else:
                    mn.append(lst[i])
                
                i += 1
            
            mn_val = min(mn_val, int(''.join(mn)))
            
            #mx_diff = max(mx_diff, int(''.join(mx)) - int(''.join(mn)))
            j += 1
            
            #print(int(''.join(mn)), " this is mn")

        mx_diff = mx_val - mn_val
        return mx_diff