import sys
dic={"aaa":"123456","bbb":"888888","ccc":"333333"}

log_error_count = 0

username=input()
if username not in dic.keys():
    print('Wrong User')
    exit()
while True:       
    if username in dic.keys():
        password=input()
        if password == dic[username]:
            print('Success')
            sys.exit()
        else:
            log_error_count+=1
            #print(log_error_count)
            if log_error_count<=2:
                print('Fail,'+str(3-log_error_count)+' Times Left')
                
            else:
                print('Login Denied')
                sys.exit()
        

# print(dic)
# a=dic.keys()
# print(a)
# b=dic.values()
# print(b)