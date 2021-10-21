#Fungsi dengan return value
def kuadrat(argument):
    total = argument**2
    print('nilai kuadrat dari',argument,'adalah',total)
    return total

kuadrat(3)
print(kuadrat(2))
i = kuadrat(4)
print(i)

print('-'*50)

#Fungsi dengan return value dan multiple argument
def penjumlahan(argument1,argument2):
    jumlah = argument1 + argument2
    print(argument1,'+',argument2,'=',jumlah)
    return jumlah

i = penjumlahan(10,20)
print(i)

def perkalian(argument1,argument2):
    kali = argument1 * argument2
    print(argument1,'X',argument2,'=',kali)
    return kali

i = penjumlahan(5,10)
j = perkalian(3,penjumlahan(5,10))
print(j)