#include <iostream>
using namespace std;
#include <cmath>
//count << (insertion aperatior)
// cin >> (extravtion operatior)
// << endl: means the same as ln. (Enter)
// std::cout << "Enter num1 "; (same as prompt)
// std::cin >> num1; means read the previous prompt 
int main()
{
    int pgw;
    int len;
    int wid;
    int hi;

    std::cout << "Enter package weight in kilograms: ";
    std::cin >> pgw;

    std::cout << "Enter Package length in centermeters: ";
    std::cin >> len;

    std::cout << "Enter package Width in centermeters: ";
    std::cin >> wid;

    std::cout << "Enter Package hight in centermeters: ";
    std::cin >> hi;

    // math;
    double cubic = (len * wid *hi);
    if (pgw > 27)
    {
        std::cout << "Too heavy. ";
    }
    else if (pgw > 27 && cubic > 100000)
    {
        std::cout << "Too heavy and Too Large. ";
    }
    else if (cubic > 100000)
    {
        std::cout << "Too large. ";
    }



}/*
Enter package weight in kilograms: 32
Enter Package length in centermeters: 10
Enter package Width in centermeters: 25
Enter Package hight in centermeters: 38
Too heavy.
*/