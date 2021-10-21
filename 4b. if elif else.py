makanan = ['pizza','burger','spagetti','steak']
pilih = input('masukkan menu makanan anda :')

if pilih in makanan:
    print('menu makanan',pilih,'yang anda pilih tersedia')

if pilih not in makanan:
    print('menu makanan',pilih,'yang anda pilih tidak tersedia')

