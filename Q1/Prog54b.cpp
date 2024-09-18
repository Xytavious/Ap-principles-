#include <iostream>
using namespace std;
//count << (insertion aperatior)
// cin >> (extravtion operatior)
// << endl: means the same as ln. (Enter)
// std::cout << "Enter num1 "; (same as prompt)
// std::cin >> num1; means read the previous prompt 
int main() 
{
  int num1;
  int num2;
  int num3;
  int num4;

  std::cout << "Enter num1 ";
  std::cin >> num1; 

  std::cout << "Enter num2 ";
  std::cin >> num2;

  std::cout << "Enter num3 ";
  std::cin >> num3;

  std::cout << "Enter num4 ";
  std::cin >> num4;

  int sum = num1 + num2 + num3 + num4;

  double avg = sum / 4;




  std::cout << "the sum is " << sum << endl;

  std::cout << "The Average is " << avg << endl;

  return 0;
}
/*/
Enter num1 45
Enter num2 45
Enter num3 274
Enter num4 45
the sum is 409
The Average is 102
*/
    

