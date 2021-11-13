f = open("sensor-data-1k.txt", "r")
sum = 0
for line in f.readlines():
    a = line.split(' ')
    sum += float(a[-2])
ave = sum/1000
print(format(ave, '.2f'))
