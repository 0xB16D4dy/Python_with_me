from math import sqrt 
try:
    a,b,c = map(float,input().split())
    if (a==0 and b==0 and c==0):
        print("phương trình có vô số nghiệm")
    elif (a==b==0 and c!=0):
        print("phương trình vô nghiệm")
    elif (a==0 and b!=0 and c!=0):
        print("phương trình có nghiệm là {}".format(-c/b))
    elif (a==0 and c==0 and b!=0):
        print("phương trình có nghiệm là {}".format(-c/b))
    # cách giải của kteam
    # if a==0:
    #     if b==0:
    #         if c==0:
    #             print("phương trình có vô số nghiệm")
    #         else:
    #             print("phương trình vô nghiệm")
    #     else:
    #          print("phương trình có nghiệm là {}".format(-c/b))
    else:
        delta = pow(b,2)-4*a*c
        x1 = (-b+sqrt(delta))/(2*a)
        x2 = (-b-sqrt(delta))/(2*a)
        if (delta < 0 ):
            print("phương trình vô nghiệm!")
        elif (delta == 0):
            print("phương trình có nghiệm kép x1 = x2 =", x1)
        elif (delta > 0):
            print("phương trình có 2 nghiệm phân biệt x1={}, x2={}".format(x1,x2))    
    
except ValueError:
    print("Error value!!")