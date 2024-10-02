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

    if (numC >0 && numC < 99)
    {
        per = 0.30;
        
    }
    else if (numC >= 100 && numC < 499)
    {
        per = 0.28;
        
    }
    else if (numC >=500 && numC < 749)
    {
        per = 0.27;
        
    }
    else if (numC >= 750 && numC < 1000)
    {
        per = 0.26;
        
    }
    else if (numC > 1000)
    {
        per = 0.25;
        
    }
    

    tot = numC*per;

    std::cout<<"Price per is " << per <<endl;
    std::cout<<"Your total is " << tot <<endl;

}
/*
Enter the number of copies to be printed: 1001
Price per is 0.25
Your total is 250.25
*/