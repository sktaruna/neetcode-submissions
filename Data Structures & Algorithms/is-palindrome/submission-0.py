class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-zA-Z0-9]','',s)
        cleaned=cleaned.lower()
        a=-1
        flag=0
        for i in range(0,math.floor(len(cleaned)/2)):
            if cleaned[i]==cleaned[a]:
                a-=1
                continue
            else:
                flag=1
        if flag==0:
            return True
        else:
            return False  