n=eval(input())
sum=0
sum1=1
for i in range(1,n+1):
	for j in range(1,i+1):
		sum1=j*sum1
		#print('sum1={:.0f}'.format(sum1))
		
	sum=sum+sum1
	sum1=1
	#print('sum={:.0f}'.format(sum))
print(sum)
