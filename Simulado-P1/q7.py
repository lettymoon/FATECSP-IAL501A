def gm(i,j,m={}):

    if i==j: return 1
    if (i,j) not in m:
        if i>j: m[(i,j)] = gm(i-1,j) + gm(i,j+1)
        else: m[(i,j)] = gm(i+1,j) + gm(i,j-1)
    return m[(i,j)]