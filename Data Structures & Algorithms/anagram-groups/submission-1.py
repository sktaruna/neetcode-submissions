class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list=[]
        for i in range(0,len(strs)):
            if len(strs)==0:
                break
            first=strs[0]
            temp_list=[]
            word1={}
            for j in first: # dictionary for first word in the list
                if j not in word1:
                    word1[j]=1
                else:
                    word1[j]+=1
                    
            for j in range(1,len(strs)): #parse through rest of the list
                word2={}
                if len(first)==len(strs[j]): # matching the length of the words
                    for k in strs[j]: # dictionary for second word
                        if k not in word2:
                            word2[k]=1
                        else:
                            word2[k]+=1
                    if word1==word2:
                        temp_list.append(strs[j])
            temp_list.append(first)
            final_list.append(temp_list)
            for x in temp_list:
                strs.remove(x)
        return final_list




