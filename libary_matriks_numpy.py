import numpy as np

#1 Membuat matriks awal
matriks_awal = np.array([[2, 6], [3, 9]])
print("Matriks Awal:\n", matriks_awal)

#2 Jumlah seluruh elemen
hasil_jumlah = np.sum(matriks_awal)
print("Jumlah seluruh elemen:", hasil_jumlah)

#3 Transpose matriks
transpose = np.transpose(matriks_awal)
print("Hasil transpose:\n", transpose)

#4 Membuat dua matriks
matriks1 = np.array([[2, 6], [3,94]])
matriks2 = np.array([[5, 8], [7, 11]])
print("Matriks 1:\n", matriks1)
print("Matriks 2:\n", matriks2)

#5 Perkalian matriks
hasil_kali = np.matmul(matriks1, matriks2)
print("Hasil perkalian:\n", hasil_kali)

#6 Mencari determinan
determinan = np.linalg.det(matriks_awal)
print("Determinan matriks:", determinan)

#7 Mencari invers
try:
    invers = np.linalg.inv(matriks_awal)
    print("Invers matriks:\n", invers)
except np.linalg.LinAlgError:
    print("Matriks tidak memiliki invers.")

