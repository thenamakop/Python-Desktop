matrix=[
    [0,1,1,0,0],
    [1,0,1,0,0],
    [1,1,0,1,1],
    [0,0,1,0,0],
    [0,0,1,0,0]
]

visted=[0,0,0,0,0]

def dfs(i):
    print(i)
    visted[i]=1
    for j in range(len(visted)):
        if matrix[i][j]==1 and visted[j]==0:
            dfs(j)
            
dfs(2)