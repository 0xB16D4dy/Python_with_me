#cách nhập cùng lúc nhiều biến
x, y = input("nhập lần lượt x và y: ").split()
print("hello")
print("giá trị của x là ", x)
print("giá trị của y là, ", y) 

#cách nhập cùng lúc bằng  List comprehension 
x,y,z =[int(x) for x in input("nhập các giá trị x, y, z: ").split()]
print("x = ", x)
print("y = ", y)
print("z = ", z)