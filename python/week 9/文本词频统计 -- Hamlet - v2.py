f = open("hamlet.txt", "r")
gets = f.read()

for ch in '：!#$%&()*+,-./:;<=>?@[\\]^_‘{|}~/""':
    gets = gets.replace(ch, ' ')
gets = gets.lower()
words = gets.split()

ans = {}
for word in words:
    ans[word] = ans.get(word, 0)+1

res = list(ans.items())

res.sort(key=lambda x: x[1], reverse=True)
n = int(input())
for j in range(n):
    word, count = res[j]
    print("{0:<10}{1:>5}".format(word, count))
