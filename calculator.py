import welcome
import matematika

welcome.welcome_massage('SELAMAT DATANG!', 'KALKULATOR GEN Z PYTHON','V1.0')
welcome.aturan_program(nama = input('Masukkan nama kamu: '))

while True:
    operator = input('Masukkan operator yang ingin digunakan: ')

    if operator == '+':
        Hasil = matematika.penjumlahan(angka1 = int(input('Masukkan angka pertama: ')), angka2 = int(input('Masukkan angka kedua: ')))
        print(f'Hasilnya = {Hasil}')
    elif operator == '-':
        Hasil = matematika.pengurangan(angka1 = int(input('Masukkan angka pertama: ')), angka2 = int(input('Masukkan angka kedua: ')))
        print(f'Hasilnya = {Hasil}')
    elif operator == '*':
        Hasil = matematika.perkalian(angka1 = int(input('Masukkan angka pertama: ')), angka2 = int(input('Masukkan angka kedua: ')))
        print(f'Hasilnya = {Hasil}')
    elif operator == '/':
        Hasil = matematika.pembagian(angka1 = int(input('Masukkan angka pertama: ')), angka2 = int(input('Masukkan angka kedua: ')))
        print(f'Hasilnya: {Hasil}')
    else:
        print('Input tidak valid!')
    
    stop = input('Ketik N jika ingin berhenti, dan tekan ENTER jika ingin mengitung lagi: ')

    if stop == '':
        print('Baik, program dilanjutkan!')
    else:
        print('exit program')
        break
