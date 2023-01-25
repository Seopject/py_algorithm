st_num = list(range(1,31))
hw_num = []
for i in range(28):
    hw_num.append(int(input))

for j in st_num:
    if j not in hw_num:
        print(j)