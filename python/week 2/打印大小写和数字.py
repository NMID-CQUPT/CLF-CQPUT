str=input()
int_count=0
A_count=0
a_count=0
for i in str:
    if i.isupper():
        A_count+=1
    elif i.islower():
        a_count+=1
    elif i.isdigit():
        int_count+=1
print(A_count)
print(a_count)
print(int_count)
        

    