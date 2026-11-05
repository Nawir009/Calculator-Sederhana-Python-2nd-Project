def penjumlahan(angka1, angka2):
    return angka1 + angka2

def pengurangan(angka1, angka2):
    return angka1 - angka2

def perkalian(angka1, angka2):
    return angka1 * angka2

def pembagian(angka1, angka2):
    if angka2 == 0:
        return "Ga Boleh dibagi dengan angka 0 Bro!"
    else:
        return angka1 / angka2

if __name__ == "__main__":
    print('Kamu tidak bisa menjalankan file ini karena ini adalah file function, kalau mau dijalankan, jalankan pada file yang mengimport file ini')