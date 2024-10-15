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
    for (int i = -12; i <=16; i++) {
            double y = (pow(i,6) -3 *pow(i,5)-93 * pow(i,4)+87*pow(i,3)+1596*pow(i,2) -1380 *i - 2800);
            std::cout << i <<"     "<<y<<endl;}

}
