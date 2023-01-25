# N개의 정수
N = int(input())
num_list = sorted(list(map(int, input().split())))
print(num_list[0], num_list[-1])