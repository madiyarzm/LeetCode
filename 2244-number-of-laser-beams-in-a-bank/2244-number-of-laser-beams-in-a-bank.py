class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        #remove rows with no devices
        #count devices using .count
        #sum connections between adjacent non-empty rows, by multiplying

        counts = [0] * len(bank)

        for row in bank:
            row_count = row.count("1")

            if row_count > 0:
                counts.append(row_count)

        lasers = 0    
        for i in range (1, len(counts)):
            lasers += counts[i - 1] * counts[i]
        
        return lasers


        
                

