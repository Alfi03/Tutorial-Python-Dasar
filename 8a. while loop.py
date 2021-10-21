angka = 0
while angka < 5:
    print('nilai angka adalah',angka)
    angka += 1

print('-'*50)

start = True
angka = 0
while start:
    print('di dalam while')
    if angka is 50:
        start = False
        print('angka 50 di temukan')
    angka += 1