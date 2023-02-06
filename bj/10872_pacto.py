# n까지의 팩토리얼
def pacto(n, ans=1):
    if n == 0:
        return ans
    ans = ans * n
    return pacto(n-1, ans)

print(pacto(int(input())))