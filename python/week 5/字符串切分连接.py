sent = input().split(" ")
m = input()
# print(sent())
ls = list()
for i in range(len(sent)):
    ls.append(sent[i])
    ls.append(m)
for j in range(len(ls)-1):
    print(ls[j], end="")
