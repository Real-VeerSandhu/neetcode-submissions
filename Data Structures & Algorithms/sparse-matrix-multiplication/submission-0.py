class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        M = len(mat1)
        K = len(mat1[0])
        k = len(mat2)
        N = len(mat2[0])

        res = [[0] * N for _ in range(M)]

        for i in range(M):
            for p in range(K):
                for j in range(N):
                    res[i][j] += mat1[i][p] * mat2[p][j]

        return res