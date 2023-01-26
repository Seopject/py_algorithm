test = list(input().split(' '))

if '' in test:
    while '' in test:
        del test[test.index('')] # del과 인덱스를 활용한 제거
        if '' not in test:
            print(len(test))

else:
    print(len(test))