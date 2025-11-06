class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        c = 0
        i = 0

        while i < len(colors):
            j = i
            chain = [neededTime[j]]

            while j + 1 < len(colors) and colors[j + 1] == colors[j]:
                chain.append(neededTime[j + 1])
                j += 1

            if len(chain) > 1:
                c += sum(chain) - max(chain)

            i = j + 1  # move to next distinct color

        return c
