print("LIST")
data_orang = ["Bagus", "Dwi", "Bayu"]
print(data_orang)
data_orang.append("Budi")
print(data_orang)

print("\nMengakses List")
print(f"Hai {data_orang[1]}, data ke 2")

print("\nMengakses Semua List Menggunakan For-in")
for x in (data_orang):
    print(f"Hai {x}")

print("\nMengakses Semua List Menggunakan For-Range")
for x in range(len(data_orang)):
    print(f"{x+1}. Hai {data_orang[x]}")