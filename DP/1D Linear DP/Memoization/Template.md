class Solution:
    def problem(self, n: int) -> int:
        dp = [-1] * (n + 1)

        def solve(n):
            Base case
            if n == BASE:
                return ANSWER

            # Memoization
            if dp[n] != -1:
                return dp[n]

            # DP recurrence
            dp[n] = ...

            return dp[n]

        return solve(n)