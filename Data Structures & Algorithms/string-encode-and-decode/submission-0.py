class Solution:

    def encode(self, strs: List[str]) -> str:
        final_word=""
        for i in strs:
            final_word+="#3+;"
            final_word+=i
        return final_word
        #final_word.split("#3+;")[1:]    


    def decode(self, s: str) -> List[str]:
        return s.split("#3+;")[1:]
