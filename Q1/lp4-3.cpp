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
    int eggs;
    double per;
    int n2;

    std::cout<<"enter number of eggsa: ";
    std::cin >> eggs;

    if (eggs > 0 && eggs <4)
    {
        per = eggs * 0.50;
        std::cout << "number of eggs " << eggs <<endl <<"the bill is " << per;

    }
    else if (eggs >= 4 && eggs < 6)
    {
        per = eggs * 0.45;
        std::cout << "number of eggs " << eggs <<endl <<"the bill " << per;
    }
    else if (eggs >= 6 && eggs <  11)
    {
        per = eggs * 0.40;
        std::cout << "number of eggs " << eggs <<endl <<"the bill " << per;
    }
    else if (eggs > 11)
    {
        per = eggs * 0.35;
        std::cout << "number of eggs " << eggs <<endl <<"the bill " << per;

    }
}