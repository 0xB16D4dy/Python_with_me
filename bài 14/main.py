from os import error


member1, age1 = input().split()
member2, age2 = input().split()

try:
    age1=int(age1)
    age2=int(age2)
    if age1<=0 or age2<=0:
        print("tuổi phải là số dương")
    elif age1>age2:
        print(member1, ' > ', member2)
    elif age2>age1:
        print(member1,' < ', member2)
    else:
        print(member1, ' = ', member2)
except:
    print("đầu vào ko hợp lệ")
