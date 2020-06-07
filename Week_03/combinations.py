class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []
        # 对应函数
        self.__dfs(1, k, n, [], res)
        return res
    

    def __dfs(self, start, k, n, prv, res):
        if len(prv) == k:
            res.append(prv[:])
            return  
        
        for i in range(start, n - (k - len(prv)) + 2):
            prv.append(i)
            self.__dfs(i+1, k, n, prv, res)
            prv.pop()