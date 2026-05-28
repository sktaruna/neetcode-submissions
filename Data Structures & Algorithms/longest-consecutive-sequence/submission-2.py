class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums=list(set(nums))
        occ=[0,0]
        def check(seq):
            while len(seq) > 0:
                count = 1
                minimum = min(seq)
                while (minimum + count) in seq:
                    count += 1
                if count > occ[1]:
                    occ[0] = minimum
                    occ[1] = count
                seq.remove(minimum)
                for i in range(0, count):
                    if (minimum + i + 1) in seq:
                        seq.remove(minimum + i + 1)
            return occ[1]
        return check(nums)
        