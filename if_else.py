# == sama dengan, != tidak sama, >= besar sama, <= kecil sama
# urutan print, if, elif, else

a = 2
b = 1

if a > b:
    print('a is greater than b')

elif a < b:
    print('a is not greater than b')

else:
    print('a sama dengan b')

#penggunaan and, or, not

a = 10
b = 5
c = 1

#penggabungan dua kondisi menggunakan and (kedua nilai harus true), or (satu nilai true)
if a > c and a > b:
    print('a merupakan bilangan terbesar')

print(a < b and b > c)
print (a < b or b > c)
print (not a < b)

