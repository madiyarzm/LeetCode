class Solution:
    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        words = {
            0: "Zero",
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
            20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty",
            70: "Seventy", 80: "Eighty", 90: "Ninety",
            100: "Hundred", 1000: "Thousand", 1000000: "Million", 1000000000: "Billion"
        }

        def helper(x):
            result = []

            if x == 0:
                return ""

            if x < 20:
                return words[x]

            if x >= 100:
                result.append(words[x // 100] + " " + words[100])
                rem = x % 100
                if rem != 0:
                    # avoid infinite recursion when remainder < 100
                    if rem < 100:
                        if rem < 20:
                            result.append(words[rem])
                        else:
                            tens = (rem // 10) * 10
                            ones = rem % 10
                            result.append(words[tens])
                            if ones != 0:
                                result.append(words[ones])
                    else:
                        result.append(helper(rem))
            else:
                tens = (x // 10) * 10
                ones = x % 10
                if tens != 0:
                    result.append(words[tens])
                if ones != 0:
                    result.append(words[ones])

            return " ".join(result)

        n = num
        result = []
        labels = ["", "Thousand", "Million", "Billion"]

        i = 0
        while n > 0:
            current = n % 1000
            if current != 0:
                result.append(helper(current) + (" " + labels[i] if labels[i] else ""))
            n //= 1000
            i += 1

        answer = " ".join(reversed(result))
        return answer.strip()
