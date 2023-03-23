n = int(input())
A = []
for i in range(n):
    A.append(list(map(int, input().split(" "))))
def trace(A):
    res =0
    for i in range(0,n):
        res += A[i][i]
    return(res)
#for c in A:
    #print(c)

print(trace(A))
