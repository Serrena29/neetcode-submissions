class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    

        present = set(nums)
        answer = []

        for i in range(1, len(nums) + 1):
            if i not in present:
                answer.append(i)

        return answer