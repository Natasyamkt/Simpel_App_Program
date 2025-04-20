import pandas as pd

# 1. Membuat data yang sederhana
data = {
    'Nama': ['nisa', 'tasya', 'asya'],
    'Umur': [17, 18, 19],
    'Kota': ['medan', 'Bandung', 'jogja']
}

# 2. Membuat DataFrame (tabel)
df = pd.DataFrame(data)

# 3. Tampilkan data
print("DataFrame Pandas:\n", df)

# 4. Menampilkan data tertentu
print("\nHanya kolom Nama dan Umur:")
print(df[['Nama', 'Umur']])
