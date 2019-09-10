
while True:
    try:
        word_1, word_2 = raw_input(), raw_input()
        m, n = len(word_1), len(word_2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word_1[i-1] == word_2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
        print dp[m][n]
    except:
        break
