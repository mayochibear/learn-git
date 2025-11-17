from math import sqrt as sqrt

a = float(input("a: "))
b = float(input("b: "))
c = sqrt(pow(a, 2) + pow(b, 2))
print(f"The hypotenuese of the triangle is {round(c, 2)}")