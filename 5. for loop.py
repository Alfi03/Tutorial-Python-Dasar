# list sebagai iterable
minuman = ['coffe','fanta','coca-cola','sprite','coklat']
for i in minuman:
    print(i)
    print(len(i))

# string sebagai iterable
makanan = 'pizza'
for i in makanan:
    print(i)

# for di dalam for
gorengan = ['tahu','bakwan','tempe','pisang']
buah = ['semangka','apel','anggur','jeruk']
sayur = ['kangkung','wortel','tomat','kentang']

daftarBelanja = [gorengan,buah,sayur]

for subDaftarBelanja in daftarBelanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)