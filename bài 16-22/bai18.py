a, b, c = input().split()
a = float(a)
c = float(c)
if b=="+":
    print("{} {} {} = {}".format(a,b,c,a+c))
elif b=="-":
    print("{} {} {} = {}".format(a,b,c,a+c))
elif b=="*":
    print("{} {} {} = {}".format(a,b,c,a+c))
elif b=="/":
    if c!=0:
        print("{} {} {} = {}".format(a,b,c,a+c))
    else: 
        print("mẫu số phải khác 0")

