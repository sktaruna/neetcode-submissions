from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper=defaultdict(int)
        result=[]
        for i in nums:
            mapper[i]+=1
        mapper1=dict(sorted(mapper.items(), key=lambda item: item[1], reverse=True))
        key_list=list(mapper1.keys())
        key=key_list[0:k]
        return key
            

        