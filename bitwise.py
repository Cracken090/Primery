a = 10
b = 5
print ( 'a =' , a , '\tb = ' , b )
# 1010 ^ 0101 = 1111 (десятичное 15)
a = a ^ b
# 1111 ^ 0101 = 1010 (десятичное 10)
b = a ^ b
# 1111 ^ 1010 = 0101 (десятичное 5)
b = a ^ b
print ( 'a =' , a , '\tb = ' , b )