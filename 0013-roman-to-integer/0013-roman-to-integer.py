class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        i = 0
        
        while i < len(s):
            # Check for two-character subtractive combinations
            if i < len(s) - 1:
                if s[i] == "I" and s[i + 1] == "V":
                    num += 4
                    i += 2
                elif s[i] == "I" and s[i + 1] == "X":
                    num += 9
                    i += 2
                elif s[i] == "X" and s[i + 1] == "L":
                    num += 40
                    i += 2
                elif s[i] == "X" and s[i + 1] == "C":
                    num += 90
                    i += 2
                elif s[i] == "C" and s[i + 1] == "D":
                    num += 400
                    i += 2
                elif s[i] == "C" and s[i + 1] == "M":
                    num += 900
                    i += 2
                else:
                    # If no subtractive combination, add the single character value
                    if s[i] == "I":
                        num += 1
                    elif s[i] == "V":
                        num += 5
                    elif s[i] == "X":
                        num += 10
                    elif s[i] == "L":
                        num += 50
                    elif s[i] == "C":
                        num += 100
                    elif s[i] == "D":
                        num += 500
                    elif s[i] == "M":
                        num += 1000
                    i += 1
            else:
                # Handle the last character
                if s[i] == "I":
                    num += 1
                elif s[i] == "V":
                    num += 5
                elif s[i] == "X":
                    num += 10
                elif s[i] == "L":
                    num += 50
                elif s[i] == "C":
                    num += 100
                elif s[i] == "D":
                    num += 500
                elif s[i] == "M":
                    num += 1000
                i += 1
        
        return num
