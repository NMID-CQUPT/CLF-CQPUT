x , y= map(int,input().split()) #x animal y leg
a=True
rabbit=0
while a==True:
    rabbit+=1
    duck = x - rabbit
    Leg = 2 * duck
    rabLeg = 4 * rabbit
 
    if(Leg + rabLeg>y or duck <0):
        print("Data Error!")
        a=False
        break

    if (Leg + rabLeg == y ):
        print("{0} {1}".format(str(duck), str(rabbit)))
        break
