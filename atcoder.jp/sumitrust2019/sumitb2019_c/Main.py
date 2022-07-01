x=int(input())
count=0
chk=5
y=x%100

if x<100:
    print(0)
else:
    if y!=0:
        for i in range(x//100):
            z=y%10
            #print(y,z,chk)
            if y==0:
                break
            if z == 0:
                chk=5
                y-=chk
            elif  z > chk:
                #print("a")
                chk=5
                y-=chk
            elif z==chk:
                #print("b")
                y-=chk
            else:
                #print("c")
                chk=z
                y-=chk


        if y!=0:
            print(0)
        else:
            print(1)
    else:
        print(1)