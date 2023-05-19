n=int(input())
lis=[]
for i in range(0,n):
    split_cmd=input().split(" ")
    cmd=split_cmd[0]

    if cmd == "insert":
        lis.insert(int(split_cmd[1]),int(split_cmd[2]))
    elif cmd == "print":
        print(lis)
    elif cmd == "remove":
        lis.remove(int(split_cmd[1]))
    elif cmd == "append":
        lis.append(int(split_cmd[1]))
    elif cmd == "sort":
       lis.sort()
    elif cmd == "pop":
        lis.pop()
    elif cmd == "reverse":
        lis.reverse()

