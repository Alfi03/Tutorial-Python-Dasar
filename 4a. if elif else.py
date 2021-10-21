angka = int(input('masukkan angka :'))
if angka == 100:
    print('nilai anda', angka)

if angka is 100:
    print('nilai anda',angka)

if angka is not 100:
    print('nilai anda bukan 100')

print(50*'-')
pilih = 'Y'
while(pilih == 'Y') or (pilih == 'y'):
    nilai1 = int(input('masukkan nilai anda :'))
    if 80 <= nilai1 <= 100:
        print('nilai anda adalah A')
    elif 70 <= nilai1 < 80:
        print('nilai anda adalah B')
    elif 60 <= nilai1 < 70:
        print('nilai anda adalah C')
    elif 50 <= nilai1 < 60:
        print('nilai anda adalah D')
    elif 40 <= nilai1 < 50:
        print('nilai anda adalah E')
    else:
        print('maaf, anda tidak lulus mata kuliah ini')
    pilih = input("Ingin input nilai lagi ? (tekan Y untuk lanjut) :")
    print('\n')