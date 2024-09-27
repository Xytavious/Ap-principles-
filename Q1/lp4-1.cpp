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
    double per = 0.25;
    double tot;
    int numC;

    std::cout<<"Enter the number of copies to be printed: ";
    std::cin>>numC;

    tot = numC*per;

    std::cout<<"Price per is " << per <<endl;
    std::cout<<"Your total is " << tot <<endl;

}
/*
Enter the number of copies to be printed: 1001
Price per is 0.25
Your total is 250.25
*/