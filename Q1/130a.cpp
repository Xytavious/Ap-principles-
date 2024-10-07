#include <iostream>
using namespace std;
#include <cmath>
//count << (insertion aperatior)
// cin >> (extravtion operatior)
// << endl: means the same as ln. (Enter)
// std::cout << "Enter num1 "; (same as prompt)
// std::cin >> num1; means read the previous prompt 

// work note if you mod it by 2 and it reterns 0 its even and if it does not its odd
int eve(int x)
{
   return x * 2;
} 

double od(int c)
{
   return (c *3) +1;
}
void loop()
{
   
}
int main()
{

    

    int num1; 
    std::cout << "Enter Number ";
    std::cin >> num1;
    int jimmy = num1 % 2;
    int even;
    int odd;
    int res;




    if (jimmy = 0 )
    {
        // even = num1;
         res = eve(num1);

    }
    else if (jimmy != 0 )
    {
        // odd = num1;
         res = od(num1);

    }
    std::cout<<"Somthing "<< res;


}