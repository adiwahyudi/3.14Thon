#Library
import os
import sys

#Tipe Data (Ngecek Tipe Data)

a = 5
print (a,"adalah tipe ",type(a))
a = 2.0 
print (a,"adalah tipe ",type(a))
a = 1+2j
print (a,"apakah angka kompleks ?", isinstance(a,complex))

#array
x = [0]*10005;       #ngisi array 0 sebanyak 10, x[0] = 0
x[1] = 1;

for j in range (2,10001):
    x[j] = x[j-1]+x[j-2]
#print(x[10000])

# Float atau bilangan pecahan dibatasi akurasinya pada 15 desimal. 

#String 
s = "Hello World!"
print(s[4])         #ngambil char ke 4 dari s dengan itungan array
print(s[6:11])      #ngambil dari char ke 6 sampe 10 dengan itungan array, dari 6 sampe 11-1 (10) emang gtu ngitungnya


#List 

x = [5,10,15,20,25,30,35,40]
print(x[5])                 
print(x[-1])            #dari yg paling belakang
print(x[3:5])           
print(x[:5])            #dari idx 0-5    
print(x[-3:])           #idx dari 3 terbelakang
print(x[1:7:2])         # index 1 hingga sebelum index 5, dengan "step" 2 (dalam hal ini hanya index 1, 3, 5)

#Input

#a = input('Masukan inputan: ')
"""
feeling = input('How are you?')
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')
"""
print('Hello'.upper())
print('Hello'.upper().lower())
print('Hello'.upper().lower().upper())
print('HELLO'.lower())
print('HELLO'.lower().islower())

'abcde'.islower()
"""
isalpha() mengembalikan True jika string berisi hanya huruf dan tidak kosong.
isalnum() mengembalikan True jika string berisi hanya huruf atau angka, dan tidak kosong.
isdecimal() mengembalikan True jika string berisi hanya angka/numerik dan tidak kosong.
isspace() mengembalikan True jika string berisi hanya spasi, tab, newline, atau whitespaces lainnya dan tidak kosong.
istitle() mengembalikan True jika string berisi kata yang diawali huruf kapital dan dilanjutkan dengan huruf kecil seterusnya.


while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')
while True:
    print('Select a new password (with capital letters and numbers only):')
    password = input()
    if password.isalnum() and password.istitle():
        break
    print('Passwords can only have letters and numbers.')

"""
3 * 5
for i in range (3, 5):
    print(i)

"""kalkulator"""
 
class Kalkulator:
    """kalkulator tambah kurang"""
    def __init__(self, _i):
        self.i = _i
 
    def tambah(self, _i): return self.i + _i
 
    def kurang(self, _i):
        return self.i - _i  

a = 1
if a % 2 == 0:
    print('bilangan {} adalah genap'.format(a))
else:
    print('bilangan {} adalah ganjil'.format(a))