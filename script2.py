# Ngambil Folder GitHub nya Kelas Terbuka
# Jangan lupa Subscribe Kelas Terbuka


import requests,os
os.system('setterm -foreground yellow')
os.system('clear')

def keluar():
  y = ['Y','y']
  n = ['n','N']
  tanya = input ('Apakah Kamu mau Keluar (y/n) ?')
  if tanya in y:
    os.system('exit')
  elif tanya in n:
    os.system('python script2.py')
  else:
    print("Yang kamu masukkan bukan y atau n")
    os.system('exit')

# Akhir dari fungsi keluar
    
def java():
  os.system('https://github.com/kelasterbuka/JAVA_dasar_programming.git')
  
# Akhir dari fungsi java

def python():
  os.system('pkg install python')
  os.system('pkg install nano')
  os.system('pip install requests')
  os.system('pkg install vim')
  os.system('https://github.com/kelasterbuka/Python3.x_Dasar_Programming.git')
  
# Akhir dari fungsi python
  
def cpp():
  os.system('pkg install g++')
  os.system('pkg install clang+')
  os.system('pkg install nano')
  os.system('https://github.com/kelasterbuka/CPP_dasar-dasar-programming.git')
  
# Akhir dari fungsi Cpp



# Body Yang di tampilkan di layar  
print(50*"=")
print("Tools Belajar programming language")
print(50*"=")

print('''

|=> [1] Belajar python
|=> [2] Belajar C++
|=> [3] Belajar Java
|=> [4] Exit

''')
print(50*"=")
menu = input('|=> [?] Silahkan Pilih Menu : ')
# Akhir body

# Eksekusi Pengecekan
if menu == '1':
  python()
elif menu == '2':
  cpp()
elif menu == '3':
  java()
elif menu == '4':
  keluar()
else:
  print("perintah tidak di ketahui")
  os.system('python script2.py')
# Akhir dari pengecekan  


  
  
  
  
  
  
  
  
  

