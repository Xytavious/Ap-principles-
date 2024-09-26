#include <iostream>
using namespace std;
#include <cmath>
int main()
{
    int num1;
    int num2;
    
    std::cout << "Enter Nuber1: ";
    std::cin >> num1;

    std::cout << "enter Number2:";
    std::cin >> num2;

    std::cout << "Original Numbers are: " << num1 << " and " << num2 << endl; 

    int sum = num1 + num2;
    int diffrence = num1 - num2;
    int product = num1 * num2;
    double avg = (num1 = num2)/2;
    int Absolute_value = abs(diffrence);

   
    int Maximum;
    int Minimum; 
    
    if (num1 > num2)
    {
        Maximum = num1;
        Minimum = num2;
    }
    else if (num1< num2)
    {
        Maximum = num2;
        Minimum = num1;
    }
    else if (num1 == num2)
    {
        Maximum = num1;
        Minimum = num2;
    }
    std::cout << "Sum =    " << sum << endl;
    std::cout << "Difference =   " << diffrence << endl;
    std::cout << "Product =   " << product << endl;
    std::cout << "Average =   " << avg <<endl;
    std::cout << "Absolute value =   " << Absolute_value << endl;
    std::cout << "Maximum =   " << Maximum << endl;
    std::cout << "Minimum =   " << Minimum << endl;



}
/*
Enter Nuber1: 15
enter Number2:58
Original Numbers are: 15 and 58
Sum =    73
Difference =   -43
Product =   870
Average =   29
Absolute value =   43
Maximum =   58
Minimum =   58
*/