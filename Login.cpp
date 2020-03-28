
#include <iostream>
#include <conio.h>
#include <windows.h>
#include <unistd.h>
#include <stdio.h>
#include <cstdlib>
#include <math.h>

using namespace std;

int main(){
	string a;
	int b;
	cout << "Masukan IP/Domain website : ";
	cin >> a;
	cout << "Berapa jumlah serangan yang akkan diluncurkan : ";
	cin >> b;
	
	int i;
	for(i = 0; i < b; i++){
		cout << "menyerang" + a + i + "%"<< endl;
		Sleep(100);
	}
	
	cin.get();
	return 0;
}
 
