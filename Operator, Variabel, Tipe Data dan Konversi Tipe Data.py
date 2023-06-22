#Operator Aritmatika
#Operator Aritmatika digunakan untuk melakukan operasi matematika yang umum.
#Macam macam Operator Aritmatika, yaitu:

#(+ : Penjumlahan)
#(- : Pengurangan)
#(* : Perkalian)
#(/ : Pembagian)
#(% : Modulus)
#(** : Perpangkatan)
#(// : Pembagian dengan hasil floring)

#Penjumlahan
print('Penjumlahan')
print(2+2)
print('_'*20)
#Pengurangan
print('Pengurangan')
print(2-3)
print('_'*20)
#Perkalian
print('Perkalian')
print(2*3)
print('_'*20)
#Pembagian
print('Pembagian')
print(2/3)
print('_'*20)
#Modulus
print('Modulus')
print(3%2)
print('_'*20)
#Perpangkatan
print('Perpangkatan')
print(2**3)
print('_'*20)
#Pembagian dengan hasil pembulatan flooring
print('Pembagian pembulatan flooring')
print(3//2)
print('_'*20)

#Latihan Operator 1
#Buat Program Penerapan Operator Aritmatika
x = 24
y = 10

print('x =',x)
print('y =',y)
print('\n')
 
print('x + y =',x+y)
print('x - y =',x-y)
print('x * y =',x*y)
print('x / y =',x/y)
print('x // y =',x//y)
print('x % y =',x%y)
print('x ** y =',x**y)
print('_'*20)

#Operator Assignment
#Operator Assignment digunakan untuk menyipan nilai menjadi suatu variabel


# = : Contohnya x = 5 -> x = 5 
# += : Contohnya x = x+5 -> x += 5
# -= : Contohnya x = x-5 -> x -= 5
# *= : Contohnya x = x*5 -> x *= 5
# /= : Contohnya x = x/5 -> x /= 5
# %= : Contohnya x = x%5 -> x %= 5
# //= : Contohnya x = x//5 -> x //= 5
# **= : Contohnya x = x**5 -> x **= 5

#Penjumlahan
print('Penjumlahan')
x=5
x=x+5
print(x)
x=5
x+=5
print(x)
print('_'*20)
#Pengurangan
print('Pengurangan')
x=5
x=x-5
print(x)
x=5
x-=3
print(x)
print('_'*20)
#Perkalian
print('Perkalian')
x=5
x=x*5
print(x)
x=5
x*=3
print(x)
print('_'*20)
#Pembagian
print('Pembagian')
x=5
x=x/5
print(x)
x=5
x/=3
print(x)
print('_'*20)
#Modulus
print('Modulus')
x=5
x=x%5
print(x)
x=5
x%=3
print(x)
print('_'*20)
#Perpangkatan
print('Perpangkatan')
x=5
x=x**5
print(x)
x=5
x**=3
print(x)
print('_'*20)
#Pembagian dengan hasil pembulatan flooring
print('Pembagian pembulatan flooring')
x=5
x=x//5
print(x)
x=5
x//=3
print(x)
print('_'*20)

#Latihan Operator 2
#Buat Program Penerapan Operator Assignment

#Penjumlahan
print('Penjumlahan')
x=24
x=x+5
print(x)
x=32
x+=5
print(x)
print('_'*20)
#Pengurangan
print('Pengurangan')
x=3
x=x-2
print(x)
x=23
x-=3
print(x)
print('_'*20)
#Perkalian
print('Perkalian')
x=45
x=x*2
print(x)
x=22
x*=2
print(x)
print('_'*20)
#Pembagian
print('Pembagian')
x=6
x=x/2
print(x)
x=20
x/=5
print(x)
print('_'*20)
#Modulus
print('Modulus')
x=6
x=x%5
print(x)
x=4
x%=3
print(x)
print('_'*20)
#Perpangkatan
print('Perpangkatan')
x=2
x=x**5
print(x)
x=20
x**=3
print(x)
print('_'*20)
#Pembagian dengan hasil pembulatan flooring
print('Pembagian pembulatan flooring')
x=20
x=x//5
print(x)
x=5
x//=2
print(x)
print('_'*20)

a = 5
b = 3
b = b + 1
c = a + b
d = c + c + a
e = (c + d)* a
 
print('Isi variabel a:',a)
print('Isi variabel b:',b)
print('Isi variabel c:',c)
print('Isi variabel d:',d)
print('Isi variabel e:',e)

x = 10
x += 5
print('x += 5  :',x)
  
x = 10
x /= 5
print('x /= 5  :',x)
  
x = 10
x **= 5
print('x **= 5 :',x)
  
x = 10
x <<= 2
print('x <<= 2 :',x)
print('_'*20)

#Operator Pembanding
#Operator Pembanding digunakan untuk membandingkan dua nilai atau variabel
#Macam macam operator pembanding :

# == -> sama dengan
# != -> tidak sama dengan
# > -> lebih dari
# < -> kurang dari
# >= -> lebih dari dan sama dengan
# <= -> kurang dari dan sama dengan

print(2==2)
print(2!=2)
print(2>2)
print(2<2)
print(2>=2)
print(2<=2)
print('_'*20)

#Latihan Operator 3
#Buatlah Program Penerapan Operator Pembanding

x = 24
y = 10

print('x =',x)
print('y =',y)
print('\n')

print('x == y hasilnya',x==y)
print('x != y hasilnya',x!=y)
print('x > y  hasilnya',x>y)
print('x < y  hasilnya',x<y)
print('x >= y hasilnya',x>=y)
print('x <= y hasilnya',x<=y)
print('_'*20)

#Operator Logika
#Operator Logika digunakan untuk mengombinasikan statement statement kondisional
#Macam macam operator logika :

# and -> kondisi menjadi benar apabila semua statementnya benar
# or -> kondisi menjadi benar apabila salah satu statementnya ada yang benar
# not -> membalik hasil dari salah ke benar dan benar ke salah

print(True and False)
print(False or False)
print(not False and True)
print('_'*20)

#Latihan Operator 4
#Buatlah Program Penerapan Operator Logika

print('Hasil dari True and True   :', True and True)
print('Hasil dari True and False  :', True and False)
print('Hasil dari False and True  :', False and True)
print('Hasil dari False and False :', False and False)
 
print('\n')
 
print('Hasil dari True or True   :', True or True)
print('Hasil dari True or False  :', True or False)
print('Hasil dari False or True  :', False or True)
print('Hasil dari False or False :', False or False)
 
print('\n')
 
print('Hasil dari not True  :', not True)
print('Hasil dari not False :', not False)
print('_'*20)


#Operator Membership / keanggotaan
#Opeerator Keanggotaan digunakan untuk menguji apakah urutan disajikan dalam suatu objek
#Macam macam operator kenaggotaan

#in -> return True ketika nilai tertentu dalam sebuah urutan ada
#not in -> return True ketika nilai tertentu dalam sebuah urutan tidak ada

a=(1,2,3,4,5,6)
b=2

print(b in a)
print('_'*20)

a=(1,2,3,4,5,6)
b=7

print(b not in a)
print('_'*20)

#Latihan Operator 5
#Buatlah Program Penerapan Operator Keanggotaan Membership

a=(11,21,43,54,45,16)
b=21

print(b in a)
print('_'*20)

a=(1,22,53,74,15,16)
b=33

print(b not in a)
print('_'*20)

#Variabel
#Variabel merupakan lokal yang dapat digunakan untuk menampung sebuah data atau informasi
#Syarat syarat penamaan variabel

#Karakter karakter yang digunakan untuk penamaan variabel adalah alphabet, angka dan underscore
#Karakter pertama variabel harus berupa huruf atau garis bawah/underscore, dan tidak bisa berupa angka
#Nama sebuah variabel tida bisa menggunakan keyword atau reserved words dari bahasa python seperti for, if dan lainnya
#Karakter pada nama variabel bersifat sensitif (case-sensitif)

#Membuat Variael
Kalimat = 'ini adalah variabel'
bilangan1 = 4
bilangan2 = 2.5
bilangan3 = True
bilangan4 = 1j + 4

#Menampilkan variabel
print(Kalimat)
print(bilangan1)
print(bilangan2)
print(bilangan3)
print(bilangan4)

print('_'*20)

#Latihan 1
#Buatlah 5 variabel dengan 5 macam tipe data

var1 = 'Assalamualaikum' #String
var2 = 1234567890 # int
var3 = 0.123456789 # float
var4 = False #bool
var5 = 1j+1 #complex

print(var1)
print(var2)
print(var3)
print(var4)
print(var5)

print('_'*20)

#Tipe Data dan Konversi Tipe Data
#Tipe Data

#1. Integr atau bilangan bulat
#2. Float atau bilangan desimal
#3. String atau kalimat
#4. Boolean yang terdiri dari True dan False
#5. Complex yang merupakan bilangan kompleks

#Menampilkan tipe data
print(type(Kalimat))
print(type(bilangan1))
print(type(bilangan2))
print(type(bilangan3))
print(type(bilangan4))

print('_'*20)

#Latihan 2
#Cek tipe data variabel pada Latihan 1
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))

print('_'*20)

#Konversi Tipe Data

#Konversi tipe data integer
print(int(bilangan2))
print(int(bilangan3))

print('_'*20)

#konversi Tipe Data Float
print(float(bilangan1))
print(float(bilangan3))

print('_'*20)

#Konversi Tipe Data String
print(str(bilangan1))
print(str(bilangan2))

print('_'*20)

#Konversi Tipe Data Bool
print(bool(bilangan1))
print(bool(bilangan2))

print('_'*20)

#Konversi Tipe Data Complex
print(complex(bilangan1))
print(complex(bilangan2))
print(complex(bilangan3))

print('_'*20)

#Latihan 3
#Konversi Tipe Data Yang Telah Dibuat

#Konversi tipe data integer
print(int(var2))
print(int(var3))

print('_'*20)

#konversi Tipe Data Float
print(float(var4))
print(float(var3))

print('_'*20)

#Konversi Tipe Data String
print(str(var5))
print(str(var2))

print('_'*20)

#Konversi Tipe Data Bool
print(bool(var1))
print(bool(var2))

print('_'*20)

#Konversi Tipe Data Complex
print(complex(var4))
print(complex(var2))
print(complex(var3))

print('_'*20)
