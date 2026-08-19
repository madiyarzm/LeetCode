from collections import defaultdict
from typing import List


class Solution:

  def partitionLabels(self, s: str) -> List[int]:
    freq = defaultdict(int)
    for letter in s:
      freq[letter] += 1

    l, r = 0, 0
    letters = set()
    result = []

    while r < len(s):
      letters.add(s[r])
      freq[s[r]] -= 1

      if freq[s[r]] == 0:
        letters.remove(s[r])

      if len(letters) == 0:
        result.append(r - l + 1)
        l = r + 1

      r += 1

    return result