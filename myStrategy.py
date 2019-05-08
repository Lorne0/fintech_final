import numpy as np

# Sharpe Ratio
def sharpe_ratio(X):
    N, U, D = 150, 0.0005, -0.001

    if len(X) < N:
        return 0
    
    A = X[-N:, 4] + X[-N:, 0] - X[-N:, 3] # AdjClose + Open - Close = AdjOpen
    mu, sigma = 0, 0
    for k in range(N-1):
        mu += (A[k+1]-A[k])/A[k]
    mu /= (N-1)
    for k in range(N-1):
        sigma += ((A[k+1]-A[k])/A[k] - mu)**2
    sigma = np.sqrt(sigma/(N-2))
    sharpe = mu/sigma

    if sharpe > U:
        return 1
    elif sharpe < D:
        return -1
    else:
        return 0
 
# Sortino Ratio
def sortino_ratio(X):
    N, U, D = 150, 0.001, -0.003

    if len(X) < N:
        return 0

    A = X[-N:, 4] + X[-N:, 0] - X[-N:, 3] # AdjClose + Open - Close = AdjOpen
    mu, sigma = 0, 0
    for k in range(N-1):
        mu += (A[k+1]-A[k])/A[k]
    mu /= (N-1)
    for k in range(N-1):
        b = (A[k+1]-A[k])/A[k]-mu
        if b < 0:
            sigma += b**2
    sigma = np.sqrt(sigma/(N-2))
    sortino = mu/sigma

    if sortino > U:
        return 1
    elif sortino < D:
        return -1
    else:
        return 0

# Sterling Ratio
def sterling_ratio(X):
    N, U, D, AVG = 153, 1, -2.5, 3

    if len(X) < N:
        return 0

    A = X[-N:, 4] + X[-N:, 0] - X[-N:, 3] # AdjClose + Open - Close = AdjOpen
    mu = 0
    for k in range(N-1):
        mu += A[k+1]-A[k]
    # Count Drawdown
    DD = []
    flag = 0
    for k in range(1, len(A)):
        if A[k]<=A[k-1] and flag==0:
            flag = 1
            peak = A[k-1]
        elif A[k]>A[k-1] and flag==1:
            flag = 0
            trough = A[k-1]
            DD.append(trough-peak)
    DD = np.sort(DD)
    if len(DD)>0:
        ADD = abs(sum(DD[:AVG])/len(DD[:AVG]))
        sterling = mu/ADD
        if sterling>U:
            return 1
        elif sterling<D:
            return -1
        else:
            return 0
         
def myStrategy(pastData):
    X = pastData.values.astype(np.float32)

    a = [0,0,0]
    a[0] = sharpe_ratio(X)
    return a[0]
    a[1] = sortino_ratio(X)
    a[2] = sterling_ratio(X)

    if sum(a)>=3:
        return 1
    elif sum(a)<=-3:
        return -1
    else:
        return 0
    
    
    
    




