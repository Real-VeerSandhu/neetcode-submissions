class Solution:
    def minDistance(self, a: str, b: str) -> int:
        M = len(a)
        N = len(b)

        dp = [[0] * (N + 1) for _ in range(M + 1)]

        for i in range(M - 1, -1, -1):
            dp[i][N] = 1 + dp[i + 1][N]
        
        for j in range(N - 1, -1, -1):
            dp[M][j] = 1 + dp[M][j + 1]

        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                add = 1 + dp[i][j+1]
                delete = 1 + dp[i + 1][j]
                
                change = (1 if a[i] != b[j] else 0) + dp[i + 1][j + 1]

                dp[i][j] = min(add, delete, change)


        return dp[0][0]