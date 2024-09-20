#include <iostream>
using namespace std;

//count << (insertion aperatior)
// cin >> (extravtion operatior)
// << endl: means the same as ln. (Enter)
// std::cout << "Enter num1 "; (same as prompt)
// std::cin >> num1; means read the previous prompt 

int main(){
   int len;
   int wid;

   std::cout << "Enter Length:";
   std::cin >> len;

   std::cout << "Enter Width:";
   std::cin >> wid;

   int area = (len*wid);
   int perim = (2* len + 2*wid);

   std::cout << "The area is: " << area << endl;
   std::cout << "The perimiter is: " << perim << endl;

   return 0;

}
