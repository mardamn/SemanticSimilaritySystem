def LCSubStr(X, Y):

    m = len(X)
    n = len(Y)
    LCSuff = [[0 for k in range(n + 1)] for l in range(m + 1)]

    result = 0
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (X[i - 1] == Y[j - 1]):
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                result = max(result, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0

    for i in range(m + 1):
        for j in range(n + 1):
            if(i==m and j==n and LCSuff[i][j]==2):
                LCSuff[i - 1][j - 1] = 0
                LCSuff[i][j] = 0
            elif (i!=m and j!=n and LCSuff[i][j]==2 and LCSuff[i+1][j+1]!=3):
                LCSuff[i-1][j-1] = 0
                LCSuff[i][j] = 0
            elif(i==m and j==n and LCSuff[i][j]==1):
                LCSuff[i][j] = 0
            elif (i!=m and j!=n and LCSuff[i][j]==1 and LCSuff[i+1][j+1]!=2):
                LCSuff[i][j] = 0

    sum=[m]
    for i in range(m ):
        sum.append(0)
    res=0
    for i in range(m):
        for j in range(n + 1):
            sum[i]=sum[i]+ LCSuff[i][j]
        if(sum[i]>0):
            res=res+1
    return res / m * 100

