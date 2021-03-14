#membuat list menggunakan []

name = ['Refki', 'Andra']
print(name[0])

#membuat list secara manual menggunakan append

name = []
name.append('Refki')
name.append('Andra')
print(name[0])

#pengulangan menggunakan for in untuk print secara menyeuruh
mylist = [1, 2, 3, 4, 5, 6]
mylist.append('refki')
mylist.append('andre')
for x in mylist:
    print(x)

for x in range(5):
    print(x)
for x in range(1,5):
    print(x)

# poin ketiga dalam range adalah penambahan
for x in range(1,5,2):
    print(x)

#mencetak mylist
mylist = ['andre', 'andru', 'andra', 'andro']

for x in mylist:
    print(x)
for x in range(1,3):
    print(mylist[x])