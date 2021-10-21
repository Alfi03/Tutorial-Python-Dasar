#scope variable : local
nama = 'katty'
def rubahNama(namaBaru):
    nama = namaBaru
    print('saya rubah nama kucing saya menjadi',nama)

rubahNama('sandra')
print('nama kucing saya menjadi',nama)

print('-'*50)

#scope variable : global
nama = 'katty'
def rubahNama(namaBaru):
    global nama
    nama = namaBaru
    print('saya rubah nama kucing saya menjadi',nama)

def jenisMakanan(makanan,namaKucing):
    global nama, makan
    nama = namaKucing
    makan = makanan

rubahNama('sandra')
jenisMakanan('universal','alex')
print('nama kucing saya menjadi',nama,'dan makan',makan)