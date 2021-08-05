# Hoặc có thể khai báo import math 
import math     
from fractions import Fraction as F
from decimal import * 

getcontext().prec = 6
x = Decimal(math.pow(32,0.2) - math.pow(F(1,64),-0.25) + math.pow(F(8,27),(F(1,3))))
a = math.pow(32,0.2)
b = math.pow(F(1,64),-0.25)
c = math.pow(F(8,27),(F(1,3)))
print("Kết quả: \n", a,"\n", Decimal(b),"\n", Decimal(c))
print("\n kết quả phép tính: ",Decimal (x))
