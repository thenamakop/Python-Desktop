x = [[10,20,30],[40,50,60],[70,80,90]]
y= [[1,1,1],[2,2,2],[3,3,3]]

result = []
for i in range(len(x)):
    result.append([])
    for j in range(len(x)):
        result[i].append(0)
        for k in range(len(x)):
            result[i][j] += x[i][k] * y[k][j]
print(result)        
    