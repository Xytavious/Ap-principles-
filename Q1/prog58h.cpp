#include <iostream>
using namespace std;
#include <cmath>
int main()
{
    double Am;
    double In;
    double Comp;
    double Days;

    std::cout << "Enter num ";
    std::cin >> Am;

    std::cout << "enter intrist rate ";
    std::cin >> In;

    std::cout << "Enter Number of times compounded per year? ";
    std::cin >> Comp;

    std::cout << "Number of days at interest? ";
    std::cin >> Days;

    double num = 0.01 * In;
    double dom = Am; 
    double exp = (Am * Days)/365;
    double s = num/dom;


    double inER = Am * 1+((0.01 * In)/Days * Comp * Days/365 );
    double meh = inER - Am;

    std::cout << "Total " << inER << endl;
    std::cout << "coumpund " << meh;


}