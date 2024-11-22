def consensus(a,x,N):
    for i in range(N):
        for j in range(N):
            if(a[i,j]==1):
                x[i,j,:]=x[j,j,:]
            else:
                x[i,j,:] = x[i,j,:]
    return x