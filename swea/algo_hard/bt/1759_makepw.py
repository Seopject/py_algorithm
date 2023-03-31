m = ['a','e','i','o','u']

def func(i,L,idx):
    if i == L:
        m_cnt = 0
        s_cnt = 0
        for t in p:
            if t in m:
                m_cnt += 1
            else:
                s_cnt += 1

        if m_cnt >= 1 and s_cnt >= 2:
            print(''.join(p))

    else:
        for j in range(idx+1,C):
            p[i] = arr[j]
            func(i+1,L,j)


L, C = map(int,input().split())
arr = sorted(list(input().split()))
p = [0]*L
func(0,L,-1)