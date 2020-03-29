# Ngambil Folder GitHub nya Kelas Terbuka
# Jangan lupa Subscribe Kelas Terbuka


import requests,os
os.system('clear')

def all():
  os.system('pkg install python')
  os.system('pkg install nano')
  os.system('pip install requests')
  os.system('pkg install vim')
  os.system('https://github.com/kelasterbuka/Python3.x_Dasar_Programming.git')
  
def cls_terbk():
  os.system('pkg install g++')
  os.system('pkg install clang+')
  os.system('pkg install nano')
  os.system('https://github.com/kelasterbuka/CPP_dasar-dasar-programming.git')
  
print(50*"=")

print('''

~~~~~~~[Menu]~~~~~~~~~~
|=> [1] Belajar python
|=> [2] Belajar C++
|=> [3] Exit

''')
menu = input('|=> [?] Silahkan Pilih Menu : ')

if menu == '1':
  all()
elif menu == '2':
  cls_terbk()
elif menu == '3':
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
else:
  print("perintah tidak di ketahui")
  os.system('python script2.py')
  



