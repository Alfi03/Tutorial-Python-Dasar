for i in range(10,50,5):
    print(i)
    if i is 25:
        print('angka di temukan',i)

# menggunakan break
number2 = 60
for i in range(5,50,5):
    print(i)
    if i == number2:
        print(i,'di temukan')
        break # untuk mengakhiri perulangan(for)
else:
    print(number2,'tidak ditemukan')