N,M=map(int,input().split())
arr = [0]*N
for i in range(M):
    i,j,k=map(int,input().split())
    arr[i-1:j]=[k]*(j-i+1)
print(*arr)