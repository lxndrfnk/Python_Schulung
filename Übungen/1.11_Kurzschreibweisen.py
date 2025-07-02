# y = 10
# z = 20
# y = 5 + y   
# z = z * 2    
# y = y * z 
# z = 4 * y   
# print(y)  
# print(z)

y = 10 # y = 10
z = 20 # z = 20
y += 5 # y = 10 + 5 = 15
z *= 2 # z = 20 * 2 = 40
y *= z # y = 15 * 40 = 600
z = 4 * y # z = 4 * 600 = 2400
print(y)
print(z)