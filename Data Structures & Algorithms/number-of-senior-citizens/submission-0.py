class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for ppl in details:
            age = int(ppl[11:13])

            if age > 60:
                cnt += 1
        return cnt        

        