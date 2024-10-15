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
    for (int i = 0; i <= 20; i++) {
        
        int x = pow(i,2);
        double y = sqrt(i);
        double c = pow(i,3);
        double forth =(double) pow(i,1/4);
        std::cout<<i<<"\t"<<x<<"\t"<<y<<"\t\t"<<c<<"\t"<<forth<<endl;
    }


}