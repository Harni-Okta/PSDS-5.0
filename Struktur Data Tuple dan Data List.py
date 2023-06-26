#STRUKTUR DATA TUPLE
#Tuple adalah jenis struktur data yang tidak dapat diubah elemennya dan juga tidak dapat ditambahkan elemennya.
#Umumnya tuple digunakan untuk data yang bersifat sekali tulis, dan dapat dieksekusi lebih cepat.
#Tuple didefinisikan dengan kurung dan elemen yang dipisahkan dengan koma.

#Contoh Tuple
T1 = (1, "dua", True, 1+2j)
print("ini adalah tuple", T1)

T11 = 1, "dua", True, 1+3j
print("ini adalah tuple", T11)

#Menampilkan tipe struktur data
type(T1)

type(T11)

#Sifat-sifat tuple

#Terurut/Ordered
T1[0:3]

#Tidak Dapat Diganti/Immutable
#Contohnya -> T1[2] = "manusia" -> Hasilnya akan error

#Dapat Diindeks/Slicing
print("Elemen kedua dari tuple T1 adalah: ", T1[1])

#Tidak Dapat Menambahkan Elemen Baru
T1 = (1, "dua", True, 1+2j)
print(f'tuple\t: {T1}')

#T1.append(10)
#T1.append(50)
#print(f' tuple\t: {T1}') -> Hasilnya akan error

#Tidak dapat menghapus elemen
T1 = (1, "dua", True, 1+2j)
print(f'tuple\t: {T1}')

#T1.remove(1)
#T1.remove("dua")
#print(f ' tuple\t: {T1}') -> Hasilnya akan error

#Menggabungkan Tuple
T3 = T1 + T11
print(T3)

#Latihan 1
#Buatlah tuple sendiri

t = (1234, 4321, 'Hello')
nama = ('petani', 'kode', 'linux')

#latihan 2
#Buatlah tuple kedua lalu gabungkan 2 tuple yang telah kamu buat

a = 1234, 432, 'World!'
print(a)
x = t+nama+a
print(x)

#STRUKTUR DATA LIST
#List adalah jenis kumpula data terurut (ordered sequence), bisa diubah elemennya (mutable), bisa ditambahkan elemen baru atau menghapus elemen(changeable),
#dan merupakan salah satu variabel yang sering digunakan pada Python.
#Serupa,namun tak sama dengan array pada bahasa programanan lainnya. Bedanya, elemen List pada python
#tidak harus memiliki tipe data yang sama. Mendeklarasikan List cukup mudah dengan kurung siku dan elemen yang dipisahkan dengan koma.
#Setiap data di dalamnya  dapat diakses dengan indeks yang dimulai dat nol.

#Contoh List
L1 =[1,2,3,4,5]
print(type(L1))

L2 = ["a","Python",3]
print(type(L2))

print(L1)
print(L2)

#Sifat-sifat List
#Terurut / Ordered
print('Memanggil List L1 dengan indeks urutan:', L1[0:3])

#Bisa Diganti/Mutable
L1[1] = 2
print('List L1 setelah diganti elemennya:', L1)

L1 = [1, "dua", True, 2+3j]

#Dapat Diindeks/Slicing
print("Slicing List L1:", L1[3])

#Dapat Diijinkan Duplikasi
L1 = [1, 2, True, "tiga", 2+3j]
print("Duplikasi pada List L1:", L1)

#Dapat mengubah data dengan mengganti elemen tertentu
L1 = [1, "dua", True, 2+3j]
L1[2]=3
print("data setelah di ubah:", L1)

#Dapat menambah elemen baru pada data
L1 = [1, "dua", True, 2+3j]
L1.append(20)
print("data setelah di tambah elemennya:", L1)

#Dapat menghapus elemen pada data
L1 = [1, "dua", True, 2+3j]
L1.remove(2+3j)
print("data setelah di hapus elemennya:", L1)

#Dapat menambah elemen nya dengan fungsi extend (menambahkan elemen baru pada list namun elemen tersebut ditambahkan secara individual)
L1 = [1, "dua", True, 2+3j]
L1.extend("nanas")
print("data setelah di tambah elemennya:", L1)

#menambahkan data dengan fungsi insert(menambahkan elemen baru di list pada indeks tertentu)
L1 = [1, "dua", True, 2+3j]
L1.insert(2, 5)
print("data setelah di tambah elemennya:", L1)

#menambahkan elemen dari list menggunakan fungsi pop(menghapus berdasarkan indeks)
L1 = [1, "dua", True, 2+3j]
L1.pop(2)
print("data setelah di tambah elemennya:", L1)
