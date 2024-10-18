#include <iostream>
#include <cmath>
#include <fstream> 
#include <string>
using namespace std;
int clacP(int b){
    if (b<= 3){
        b *10;
    }
    else if (b<=6 && b>3){
        b *15;
    }

}
int main() { 
    ifstream file("data/prog505a.dat");
    if (file.is_open()){
        string first,last;
        int books;
        while (file>> first >> last >> books){

        } file.close();
    }
 }
