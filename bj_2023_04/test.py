s = '1 2 3 4'
a = list(map(int,s.split()))
answer = str(min(a))+' '+str(max(a))
print(answer)