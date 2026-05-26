class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapper={}
        for i in nums:
            if i not in mapper:
                mapper[i]=1
            else:
                mapper[i]+=1
        for i in nums:
            if mapper[i]>=2:
                return True
        return False