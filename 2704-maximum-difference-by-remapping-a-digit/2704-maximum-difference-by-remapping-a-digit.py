class Solution:
    def minMaxDifference(self, num: int) -> int:
        lst = list(str(num))
        mx_val = 0
        mn_val = float('inf')

        # Compute max
        j = 0
        while j < len(lst) and lst[j] == '9':
            j += 1

        if j < len(lst):
            first = lst[j]
            mx = []
            for ch in lst:
                mx.append('9' if ch == first else ch)
            mx_val = int(''.join(mx))
        else:
            mx_val = int(''.join(lst))  # all 9s → no change

        # Compute min
        first = lst[0]
        mn = []
        for ch in lst:
            mn.append('0' if ch == first else ch)
        mn_val = int(''.join(mn))

        return mx_val - mn_val
