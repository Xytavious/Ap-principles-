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
/*
-12     1.89728e+06
-11     982800
-10     453600
-9     173888
-8     45360
-7     0
-6     -6400
-5     0
-4     6048
-3     7280
-2     4320
-1     0
0     -2800
1     -2592
2     0
3     2240
4     0
5     -10800
6     -32032
7     -60480
8     -84240
9     -78400
10     0
11     217728
12     671840
13     1.49688e+06
14     2.8728e+06
15     5.0336e+06
16     8.27669e+06
*/