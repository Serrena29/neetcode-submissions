class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        freq = {}

        # Count frequency
        for string in arr:
            freq[string] = freq.get(string, 0) + 1

        # Find k-th distinct string
        for string in freq:
            if freq[string] == 1:
                k -= 1

                if k == 0:
                    return string

        return ""
        