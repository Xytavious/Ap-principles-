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
/*
0       0       0               0       1
1       1       1               1       1
2       4       1.41421         8       1
3       9       1.73205         27      1
4       16      2               64      1
5       25      2.23607         125     1
6       36      2.44949         216     1
7       49      2.64575         343     1
8       64      2.82843         512     1
9       81      3               729     1
10      100     3.16228         1000    1
11      121     3.31662         1331    1
12      144     3.4641          1728    1
13      169     3.60555         2197    1
14      196     3.74166         2744    1
15      225     3.87298         3375    1
16      256     4               4096    1
17      289     4.12311         4913    1
18      324     4.24264         5832    1
19      361     4.3589          6859    1
20      400     4.47214         8000    1
*/