# bài 1
# a1 = input("nhập giá trị của a1: ")
# a2 = input("nhập giá trị của a2: ")

# try:
#     a1 = int(a1)
#     a2 = int(a2)
#     print("tổng của 2 số {} và {} là: {}".format(a1,a2,a1+a2))
# except:
#     print ("định dạng không hợp lệ")
# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {} pieces of item number {} for {:.2f} dollars."
# print(myorder.format(quantity, itemno, price))
# print("I want {} pieces of item number {} for {:.2f} dollars.".format(quantity, itemno, price))


# bài 2
# sName = input()
# print("xin--chào--tôi--tên--là",sName, sep='--')
# #cách 2
# # print("xin",'chào','tôi','tên','là',sName,sep='--');

# bài 3
# dec = int(input("nhập số thập phân: "))
# c = hex(dec)
# print("Số thập phân %d trong hệ bát phân là: %o" %(dec,dec))
# print("Số thập phân %d trong thập lục phân là: %r" %(dec,c))

# bài 4
# dec = input("nhập số thập phân: ")
# try:
#     dec2 = int(dec)
#     print("Số thập phân %d trong hệ bát phân là: %o" %(dec2,dec2))
# except:  
#     print("input wrong")
# cách 2
# dec = input()
# isParse = False
# try:
#     dec = int(dec)
#     isParse = True
# except:
#     print("input wrong")

# if isParse:
#     print("Số thập phân %d trong hệ bát phân là: %o" %(dec,dec))

# bài 5
# dec = float(input())
# phay = int(input())
# kq="{0:.{1}f}"
# kqq=round(dec,phay)
# print("dùng format", kq.format(dec,phay))
# print("dùng round", kqq)


#bài 6
# dec = input()
# doc = input()
# isFloat = False
# isParse = False
# try:
#     dec = float(dec)
#     doc = int(doc)
#     print("{0:.{1}f}".format(dec,doc))
# except:
#     print("input wrong")

# bài 8
# # nhập chuỗi nhiều kí tự và tách ra
# # a =  input()
# # b = a.split()
# # dùng comprehension để nhập 
# a = [i for i in input().split()]
# s = map(int,a) # ép kiểu các chuỗi con thành kiểu int
# # print(*a) #in phần tử của list ra thành số.
# print(sum(s))

# # bài 9
# listValue = [i for i in input().split()]
# try:
#     stringValue = map(int,listValue)
#     print("tổng của danh sách là: ", sum(stringValue))
# except:
#     print("Input Wrong!!!") 