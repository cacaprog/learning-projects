 # Commom sequence strings
def common_seq(word1, word2):

    m, n = len(word1), len(word2)
    # create a 2D array to store the length of common subsequence
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # fill the dp array by comparing characters of the two words 
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else: 
                 dp[i][j] = 0
    
    # the last element of dp array contains the length of common subsequence
    return dp[m][n]

common_seq('fish', 'hish')