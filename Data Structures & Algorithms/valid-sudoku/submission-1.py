class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            mapper={}
            for j in i:  # row checker
                if j=='.':
                    continue
                elif j not in mapper:
                    mapper[j]=1
                else:
                    mapper[j]+=1
            values=list(mapper.values())
            if len(values)==0:
                continue
            elif max(values)>1:
                print("row")
                return False

        for i in range(0,9):
            mapper={}
            for j in board:  # column checker
                if j[i]==".":
                    continue
                elif j[i] not in mapper:
                    mapper[j[i]]=1
                else:
                    mapper[j[i]]+=1
            values=list(mapper.values())
            if len(values)==0:
                continue
            elif max(values)>1:
                print("column")
                return False
             

        # 3*3 checker
        box = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                result=[]
                for row in board[i:i+3]:
                    for num in row[j:j+3]:
                        result.append(num)
                box.append(result)
        
        for i in box:
            mapper={}
            print(i)
            for j in i:
                if j=='.':
                    continue
                elif j not in mapper:
                    mapper[j]=1
                else:
                    mapper[j]+=1
            values=list(mapper.values())
            print(values)
            if len(values)==0:
                continue
            elif max(values)>1:
                print("box")
                return False
             

        return True



