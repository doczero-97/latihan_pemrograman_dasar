# # 1
# x = 3
# if (x % 2) == 1:
#     print("Bilangan Ganjil")
#     if x == 3:
#         print("Angka Tiga")

# # 2
# x = 121
# if (float(x).is_integer())!=True:
#     print("Bukan bilangan bulat")
# elif(x % 2) == 1:
#     print("Bilangan ganjil")
# else:
#     print("Bilangan genap")

# # 3
# x = float(input("Masukkan angka : "))
# if (float(x).is_integer())!=True:
#     print("Bukan bilangan bulat")
# elif(x % 2) == 1:
#     print("Bilangan ganjil")
# else:
#     print("Bilangan genap")

# # 4
# x = 3 
# if ((x % 2) == 1) and (x == 3):
#     print("x adalah bilangan ganjil")

# # 5
# x = 3
# if ((x % 2) == 1) or (x == 3):
#     print("x adalah bilangan ganjil")

# # 6
# x = 11
# if ((x % 2) == 1):
#     if (x > 10):
#         print("x di atas 10")
#     elif (x == 3):
#         print("x adalah 3")
#     else:
#         print("x di bawah 10")

# 7
x = int(input("Masukkan x : "))
print(("Bilangan genap", "Bilangan ganjil") [((x % 2) == 1)])