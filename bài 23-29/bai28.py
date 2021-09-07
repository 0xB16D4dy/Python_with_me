try:
    a = int(input())
    b = int(input())
    dem = 0
    if a>b:
        print("số thứ 1 lớn hơn số thứ 2!!!")
    else:
        for i in range(a,b+1):
            if i%5==0:
                dem+=1
                if dem>10:
                    print("\nđã in quá 10 số rồi !!!")
                    break
                print(i, end=" ")
        else:
            if dem==0:
                print("không có số nào chia hết cho 5")
            else:
                print("\nđã in hết các số chia hết cho 5")
except ValueError:
    print("giá trị đầu vào không hợp lệ")

        
        