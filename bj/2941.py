word = input()

croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for i in croatian:
    cnt += word.count(i)

print(len(word) - cnt)