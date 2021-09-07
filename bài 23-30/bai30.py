while True:
    try:
        n = int(input())
    except:
        print("gia tri khong hop le")
    if n<1 or n>9:
        print("Vui long nhap so co gia tri tu 1 den 9")
    else:
        break
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print("\n")

