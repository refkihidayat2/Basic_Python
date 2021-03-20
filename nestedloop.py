#loop inside loop
#end="" berfungsi untuk menyatukan dua baris
#print("Hello", end=" ")
#print("world")

# for i in range (2):
#     for j in range(2):
#         for k in range(2):
#             print("i : {}, j : {}, k : {}". format(i, j, k), end=" ")
#     print()


# nama = []
# matkul = []
# z = 0

# n = int(input("Jumlah mahasiswa ="))
# m = int(input("Jumlah Matkul :"))
# for x in range(n):
#     name = input("Nama :")
#     nama.append(name)
#     for y in range(m):
#         matakuliah = input("Matakuliah :")
#         matkul.append(matakuliah)

# for x in range (n):
#     print(x+1," . ", nama[x])
#     for y in range (m):
#         print("--->", matkul[z])
#         z += 1


#list dua dimensi
# matkul = [[1, 2, 3], [4, 5, 6]]
# print(matkul[0][2])

for x in range(1, 11):
    for y in range(1,x+1):
        print(y, end="")
    print()

for x in range(11, 1, -1):
    for y in range(1, x):
        print(y, end=",")
    print()