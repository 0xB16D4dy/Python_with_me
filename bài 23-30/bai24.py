# for x in range(10):
#     print(x)
# else:
#     print("done!")
# i=0
# while i<10:
#     print(i)
#     i+=1
# else:
#     print("done!")
try:
    a,b = map(int,input().split())
    tong = 0
    if(a>b):
        print("số thứ nhất lớn hơn số thứ 2!!!!")
    else:
        for i in range(a,b+1):
            tong +=i
        print("tổng của các số trong khoảng từ {} đến {} là {}".format(a,b,tong))
except ValueError:
    print("định dạng đầu vào không hợp lệ!!!")