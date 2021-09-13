# cách nhập cùng lúc nhiều biến split
x, y = input("nhập lần lượt x và y: ").split()
print("hello")
print("giá trị của x là ", x)
print("giá trị của y là, ", y)
# cách nhập cùng lúc nhiều biến bằng split
x, y = input("nhập lần lượt x và y:").split()
print("giá trị của x và của y lần lượt là {}, {}".format(x, y))

# cách nhập cùng lúc nhiều biến và type casting sử dụng hàm list()
x = list(map(int, input("Nhập nhiều giá trị : ").split()))
print("danh sách các biến: ", x)

# cách nhập cùng lúc bằng  List comprehension
x, y, z = [int(x) for x in input("nhập các giá trị x, y, z: ").split()]
print("x = ", x)
print("y = ", y)
print("z = ", z)

# cách lấy cùng lúc nhiều giá trị cùng 1 lúc:
x = [int(x) for x in input("nhập các giá trị: ").split()]
print("danh sách các biến: ", x)

# đảo ngược một chuỗi
a[::-1]

# tách chuỗi thành từng kí tự 8bit rồi dịch phải
l=[]
m=""
k = "11101010100101"
for i in range(0,len(x),8):
    l.append(x[i:i+8])
for i in l:
    i = chr((int(i,2) >> 1))
    m+=i
print(m)