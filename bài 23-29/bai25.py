try:    
    a = int(input())
    if a<1 or a>9:
        print("Chi tinh duoc bang cuu chuong 1 den 9 thoi!")
    else:
        for i in range(1,10):
            print("{} x {} = {}".format(a,i,a*i))
            i+=1
except ValueError:
    print("định dạng đầu vào không hợp lệ!!!")
