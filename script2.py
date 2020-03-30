# Ngambil Folder GitHub nya Kelas Terbuka
# Jangan lupa Subscribe Kelas Terbuka


import requests,os
os.system('setterm -foreground yellow')
os.system('clear')

def bug():
  os.system('clear')
  x = ['y','Y']
  z = ['n','N']
  bug = input('Apakah Kamu Menemukan Bug (y/n)')
  if bug in x:
    nf = input('Nama File Yang Terdapat Bug : ')
    jb = input('Jenis Bug : ')
    print(50*"=")
    print("Kami Akan Perbaiki Bug ",jb,"Terdapat di File",nf)
    print("Terima Kasih Anda Sudah Melaporkan Bug Kepada Saya")
  elif bug in z:
    os.system('python script2.py')
  else:
    os.system('python script2.py')
    

def toolv1():
  os.system('pkg update && pkg upgrade')
  os.system('pkg install bash')
  os.system('pkg install git')
  os.system('git clone https://github.com/Rajkumrdusad/onex.git')
  os.system('cd onex')
  os.system('chmod +x onex')
  os.system('chmod +x install')
  os.system('./install')
  os.system('sh install')

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
|=> [4] Tools Hacking
|=> [5] Report Bug
|=> [6] Exit

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
  toolv1()
elif menu == '5':
  bug()
elif menu == '6':
  keluar()
else:
  print("perintah tidak di ketahui")
  os.system('python script2.py')
# Akhir dari pengecekan  


  
  
  
  
  
  
  
  
  

