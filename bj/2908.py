toread = input().split(' ')
toread[0] = int(toread[0][::-1])
toread[1] = int(toread[1][::-1])
print(max(toread))