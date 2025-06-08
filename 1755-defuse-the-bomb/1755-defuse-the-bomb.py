class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0 for _ in range (len(code))]

        result = []

        for i in range(len(code)):
            total = 0
            if k > 0:
                j = 1

                while j <= k:
                    total += code[(i + j) % len(code)]
                    j += 1

            
            if k < 0:
                t = 1

                while t <= abs(k):
                    total += code[(i - t) % len(code)]
                    t += 1

            result.append(total)
        
        return result