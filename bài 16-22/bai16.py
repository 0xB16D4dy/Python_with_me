def canhtamgiac(canh, canh2):
    return(canh+canh2)

try:
    #hàm map(kiểu dữ liệu muốn ép,giá trị được ép) dùng map duyệt các phần tử để ép kiểu
    canh, canh2, canh3 = map(float,input().split())
    if ((canhtamgiac(canh,canh2)>canh3) and (canhtamgiac(canh2,canh3)>canh) and (canhtamgiac(canh,canh3)>canh2)):
        print(canh,",",canh2,",",canh3," là 3 cạnh của tam giác")
    else:
        print(canh,",",canh2,",",canh3," không phải 3 cạnh của tam giác")
        # print("{}, {}, {}, không phải là 3 cạnh của tam giác".format(canh,canh2,canh3))
except ValueError:
    print("nhập giá trị sai!!!")
