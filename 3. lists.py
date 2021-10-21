data1 = [0,2,4,6,8,10]
data2 = [1,3,5,7,9,11]

#akses list
subData1 = data1[3]
subData2 = data1[-2]

#potong list
subData3 = data1[0:4]
subData4 = data1[3:]
subData5 = data1[:4]
subData6 = data1[-4:]
subData7 = data1[:-4]

#tambah list
dt = data1 + data2

#merubah isi list
data1[2] = 400
data2[2] = 500

#merubah content list dengan menggunakan metode slicing
data1[3:5] = [600,800]
data2[3:5] = [700,900]

#list di dalam list
x = [data1,data2]

#mengakses list dalam multidimentional list
y = x[1][3]

#methods untuk list
data1.append(30)

#function yang bisa kita gunakan dalam list
panjangList = len(data1)

#output
print(data1)
print(panjangList)

