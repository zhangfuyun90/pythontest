a=1
while a<=100:
    if a%7>0 and a%10!=7 and int(a/10)!=7:
        print(a)
    a+=1

