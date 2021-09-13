#!/usr/bin/env python3
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