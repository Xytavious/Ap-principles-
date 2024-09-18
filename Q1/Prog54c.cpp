#include <iostream>
using namespace std;
#include <cmath>


int main()
{
    double rad; 
    double area;
    double cir; 
     
    std::cout << "Enter Radius: "; 
    std::cin >> rad;

    area = 3.14159* pow(rad,2);
    cir = 2 * 3.14159 * rad;

    std::cout << "The radius is: " << area <<endl;
    std::cout << "the circumference: " << cir << endl;

}
/*
Enter Radius: 54
The radius is: 9160.88
the circumference: 339.292
*/