class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dic = {}
        for edge in edges:
            if edge[0] not in dic:
                dic[edge[0]] = 1
            else:
                dic[edge[0]] +=1 
            if edge[1] not in dic:
                dic[edge[1]] = 1
            else:
                dic[edge[1]] +=1
        n = len(edges)
        highest = list(dic.keys())[0]
        for key in dic:
            if dic[key] > dic[highest]:
                highest = key
        return highest
        