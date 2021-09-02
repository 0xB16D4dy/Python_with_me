try:
    with open("E:\Tài liệu\python\Python_with_me\\bài 16-22\\input.inp", "r",encoding="utf-8") as inp:
        datastring = inp.readline().rstrip("\n")

    while True:
        a,b,c = map(float,datastring.split())

        if a<0 or b<0 or c<0:
           thongbao = "ba cạnh của tam giác phải là số lớn hơn 0"
        else:
            break

    if (a + b > c) and (a + c >b) and (c + b > a):
        if (a*a==b*b+c*c) or (b*b==a*a+c*c) or (c*c==a*a+b*b):
            thongbao = "{}, {}, {} là 3 cạnh của tam giác vuông".format(a,b,c)
        elif a*a>b*b+c*c or b*b>a*a+c*c or c*c >a*a+b*b:
            thongbao = "{}, {}, {} là 3 cạnh của tam giác tù".format(a,b,c)
        elif (a==b) and (b==c):
            thongbao = "{}, {}, {} là 3 cạnh của tam giác đều".format(a,b,c)
        elif a==b or a==c or b==c:
            thongbao = "{}, {}, {} là 3 cạnh của tam giác cân".format(a,b,c)
        else:
            thongbao = "{}, {}, {} là 3 cạnh của tam giác nhọn".format(a,b,c)
    else:
        thongbao = "{}, {}, {} không phải là 3 cạnh của tam giác!!!".format(a,b,c)
except ValueError:
    print("giá trị không hợp lệ !!!")
    thongbao = "giá trị không hợp lệ !!!"
except FileNotFoundError:
    print("không tìm thấy file hợp lệ!!!")
    thongbao = "không tìm thấy file hợp lệ!!!"

with open("E:\Tài liệu\python\Python_with_me\\bài 16-22\\output.out","w", encoding="utf-8") as out:
    out.write(thongbao)
