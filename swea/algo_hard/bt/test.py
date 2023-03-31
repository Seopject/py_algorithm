arr = ['1','2','3','4','5','6']
k = 5
p = ['-','//','*','+','+']

temp = [arr[0]]
for t in range(k):
    temp.append(p[t])
    temp.append(arr[t+1])
    print(temp, end=' ')
    if temp[1] == '//' and int(temp[0]) < 0 and int(temp[2]) > 0:
        temp[0] = str(int(temp[0])*-1)
        temp = [str(eval(''.join(temp)))]
        temp[0] = str(int(temp[0])*-1)
    else:
        temp = [str(eval(''.join(temp)))]
    print(temp)

print(temp)



