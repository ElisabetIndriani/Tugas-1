a = input("Nilai Ujian Praktek= ")
b = input("Nilai Ujian Teori= ")
c=float(a)
d=float(b)
if c>=70 and d>= 70:
    print("Selamat, anda lulus!")
elif d>=70 and c<=70:
    print("Anda harus mengulang ujian praktik")
elif d<=70 and c>=70:
    print('Anda harus mengulang ujian teori')
else :
    print("Anda harus mengulang ujian teori dan praktek")