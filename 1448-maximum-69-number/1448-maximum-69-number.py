class Solution:
    def maximum69Number (self, num: int) -> int:
        
        s = str(num)
        lst = []

        for i in range(len(s)):
            lst.append(s[i])

        for i in range(len(lst)):
            if lst[i] == "6":
                lst[i] = "9"
                break
        
        return int("".join(lst))