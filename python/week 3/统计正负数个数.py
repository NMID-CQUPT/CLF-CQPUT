
count=-1
zhengshu=0
num=0
fushu=0
while True:
    m=eval(input())
    count+=1
    #print(count,'次')
    if m>0:
        zhengshu+=1
        num+=m
    elif m<0:
        fushu+=1
        num+=m
    else:
        m==0
        break
#print('总数是',num)
ave = num/count
#print(type(ave))
print(ave)
print(zhengshu)
print(fushu)
