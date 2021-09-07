while True:
    try:
        n = int(input()) 
        if 1>n or n>9:
            print("Vui long nhap gia tri tu 1 den 9!")
        else:
            break
    except:
        print("Dinh dang dau vao khong hop le!!!!" + " Vui long nhap gia tri tu 1 den 9!")
        print()

for i in range(1, n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print("\n")
