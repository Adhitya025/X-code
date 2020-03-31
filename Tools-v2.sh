#!/bin/bash

clear
figlet Grafity

read -p 'Masukan Nama : ' nama;

echo ""
echo ""
echo ""
echo "Output : "
figlet nama
echo ""
echo ""
echo ""
read -p 'Apakah Anda Ingin mulai lagi (y/n) ? ' yn;
if [ [ yn = 'y' ]  && [yn = 'Y'] ]
then
python Tools-v2.py
elif [ [ yn = 'n' ] && [ yn = 'N' ] ]
then
exit
else
echo "Perintah Tidak diketahui !"
fi
