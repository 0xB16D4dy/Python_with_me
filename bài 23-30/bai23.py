from math import sqrt
print("*************MENU*************")
print("1. Giải phương trình bậc 1")
print("2. Giải phương trình bậc 2")
selec = input("lựa chọn: ")
try:
    
    if selec=="1":
        print("vui lòng nhập các hệ số của phương trình bậc 1: \n")
        a,b = map(float, input().split())
        if (a==0):
            if (b==0):
                print("phương trình có vô số nghiệm")
            else:
                print("phương trình vô nghiệm")
        else:
            print("phương trình có nghiệm là {}".format(-b/a))
    elif selec=="2":
        print("vui lòng nhập các hệ số của phương trình bậc 2: \n")
        a,b,c = map(float, input().split())
        if a==0:
            if b==0:
                if c==0:
                    print("phương trình có vô số nghiệm")
                else:
                    print("phương trình vô nghiệm")
            else:          
                print("phương trình có nghiệm là {}".format(-c/b))
        else:
            delta = pow(b,2)-4*a*c
            if (delta < 0 ):
                print("phương trình vô nghiệm!")
            elif (delta == 0):
                print("phương trình có nghiệm kép x1 = x2 = {}".format(-b/2*a))
            elif (delta > 0):
                x1 = (-b+sqrt(delta))/(2*a)
                x2 = (-b-sqrt(delta))/(2*a)
                print("phương trình có 2 nghiệm phân biệt x1={}, x2={}".format(x1,x2))
except ValueError:
    print("giá trị không hợp lệ!!!")
