a1 = input("nhập giá trị của a1: ")
a2 = input("nhập giá trị của a2: ")

try:
    a1 = int(a1)
    a2 = int(a2)
    print("tổng của 2 số {} và {} là: {}".format(a1,a2,a1+a2))
except:
    print ("định dạng không hợp lệ")