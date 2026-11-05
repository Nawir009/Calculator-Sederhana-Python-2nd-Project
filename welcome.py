def welcome_massage(baris1,baris2,baris3):
    simbol = "=" * (max(len(baris1), len(baris2), len(baris3)) + 10)

    print(simbol)
    print(f'{baris1:=^{len(simbol)}}')
    print(f'{baris2:=^{len(simbol)}}')
    print(f'{baris3:=^{len(simbol)}}')
    print(simbol)

def aturan_program(nama):
    print(f'Halo {nama}! Operator yang tersedia:\n1. Penjumlahan (+)\n2. Pengurangan (-)\n3. Perkalian (*)\n4. Pembagian (/)')

if __name__ == "__main__":
    print('Kamu tidak bisa menjalankan file ini karena ini adalah file function, kalau mau dijalankan, jalankan pada file yang mengimport file ini')