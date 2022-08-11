print('Program Kalkulator Sederhana')
print('=' * 25)
print('Daftar Operasi Matematika')
print('  1. Jumlah \t [+]')
print('  2. Kurang \t [-]')
print('  3. Kali \t [*]')
print('  4. Bagi \t [/]')
print('=' * 25)

operasi = input('Pilih operasi (1/2/3/4): ')
print('!!Masukan bilangan bulat atau desimal!!')
bilangan_1 = eval(input('Masukkan bilangan ke-1: '))
bilangan_2 = eval(input('Masukkan bilangan ke-2: '))

print('=' * 25)

if operasi == '1':
  hasil = bilangan_1 + bilangan_2
  print(f'Hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}')
elif operasi == '2':
  hasil = bilangan_1 - bilangan_2
  print(f'Hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}')
elif operasi == '3':
  hasil = bilangan_1 * bilangan_2
  print(f'Hasil operasi dari {bilangan_1} * {bilangan_2} = {hasil}')
elif operasi == '4':
  hasil = bilangan_1 / bilangan_2
  print(f'Hasil operasi dari {bilangan_1} / {bilangan_2} = {hasil}')
else:
  print('Pilihan Tidak Dikenal')