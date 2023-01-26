word = input()

croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatian:
    if i in word:
        print(1)

print(word)