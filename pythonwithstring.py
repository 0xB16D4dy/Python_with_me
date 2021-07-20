# #tách chuỗi.
 
s = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
print(s.split(", "))
print(s[:16])
print(s[18:27])
print(s[32:42])
print(s[47:54])
print(s[60:])
print(' '.join(['Đại học Quốc gia', 'Khu phố 6', 'P. Linh Trung', 'Q. Thủ Đức', 'Tp. HCM'])) 

#viết hoa chuỗi.

#hàm viết hoa chữ cái đầu tiên của mỗi từ
def up_charec(s):
    return ' '.join(w[0].upper() + w[1:] for w in s.split(' '))

#hàm viết thường chữ cái đầu tiên
def low_charec(s):
    return ' '.join(w[0].lower()+w[1:] for w in s.split(' '))

#khai báo
s1 = "công nghệ thông tin"
supper = s1.upper()

#viết hoa chữ cái đầu tittle()
print(s1.title()) 
print(up_charec(s1))
#viết hoa hết 
print(s1.upper())
#viết thường chữ cái đầu của mỗi từ
print(low_charec(supper))
#viết hoa chữ cái đầu
print (s1[0].upper() + s1[1:])

# return ' '.join(w.capitalize() for w in s.split())    
# # or
# import string
# return string.capwords(s)
