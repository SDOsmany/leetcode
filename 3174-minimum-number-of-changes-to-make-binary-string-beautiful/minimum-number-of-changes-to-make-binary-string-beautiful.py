class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        for i in range(0, len(s), 2):
            _slice = s[i:i+2]
            if _slice != "11" and _slice != "00":
                print("not here", _slice)
                count += 1
        return count