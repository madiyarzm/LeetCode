class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        counts = [0] * len(bank)

        for row in bank:
            row_count = row.count("1")

            if row_count > 0:
                counts.append(row_count)

        lasers = 0    
        for i in range (1, len(counts)):
            lasers += counts[i - 1] * counts[i]
        
        return lasers


        
                

