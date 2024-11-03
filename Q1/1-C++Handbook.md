## C++ Handbook By Xytavious

# Basic imports
 #include <"iostream">
using namespace std; this removes the reqirement for using std::..

#include <"cmath">

count << (insertion aperatior)
cin >> (extravtion operatior)
<< endl: means the same as ln. (Enter)

## Comments

## Compiling and Running

## Data Types
* int (integer) - a whole number, positive or negative (32 bits)
* double (double-precision floating-point) - a number with a decimal (64 bits with 15 bits of precision)
* char (character) - a single keyboard (ASCII) character (1 byte)
* boolean - either true or false

## Console Input/Output


```C++ 
std::cout << "Enter num1 "; /*
(this promts the user for Input)
*/
std::cin >> num1;  /*
means read the previous prompt 
```
 Cout tell the computer the take in user input .

 while Cin tells the user to take in the user input.

## Arithmetic Operations
* '+'	Addition  Adds together two values	x + y	
* '-'	Subtracts one value from another	x - y	
* '*'	Multiplies two values	x * y	
* '/'	Divides one value by another	x / y	
* '%'	Modulus	Returns the division remainder	x % y	
* ++	Increases the value of a variable by 1	x++
* --	Decreases the value of a variable by 1	x--

## Assignment Operations 
* = this is used to set a value to a varible 
* += this adds what ever value you put after it 
* -=
## Comments

```C++
// Simple Commet

/* block
comment
across
multiple lines
*/

/* this
 * is
 * what
 * it 
 * looks
 * like
 */
```

## Decision Structures
*  If Statements: switches  
``` C++
if(condition) {
   var = X;
   do something;
} 
```
*  else statements
``` C++
else {
   var = Y;
}
```
*  Switch Statement: allows any value to change the control of the execution
```C++
int water = 3;
switch (water) {
  case 1:
    cout << "dasani ";
    break;
  case 2:
    cout << "FIJI";
    break;
  case 3:
    cout << "Wednesday";
     break;
}
```
*  Ternary: evaluates the condition and executes an expression out of two based on the result of the condition.

```C++
int main() {
  double marks;

  // take input from users
  cout << "Enter your marks: ";
  cin >> marks;

  // ternary operator checks if
  // marks is greater than 40
  string result = (marks >= 40) ? "passed" : "failed";

  cout << "You " << result << " the exam.";
```

## Conditional Operators
* '<=' Checks if a varible is less then or equal to a specified value

*  '>=' Checks if a varible is greater then or equal to a specified value

* ==: Checks if a varible is equal to a specified value

* != Checks if a varible is not equal to a specified value

## Logic Operators
* &&: and
* ||: or 
* !: not

## String Methods
* length()/size(): will return the length of the string.
```C++
std::string text = "Hello profesor ";
int length = text.length();
```
* index: Gets individual characters using an array
* at(): is used to access a character at a specified index.
* append(): The append() function adds one string to the end of another.
* 

## Random Generation
rand();

## Looping Structures
* while loop: checks the condition(<,=,>), then does the the code inside umtil the conditions are met.
```C++
int i = 1;

while (i <= 5) 
{
  cout << "Hello World"<<endl;
  i++;
}

```
* for loop
```C++
for(int i = 0; i < n; i++)
{
  // BODY
}

```
* do-while loop
```C++
int i = 2;
do {
  // loop body
  cout << "Hello World\n";
  // update expression
  i++;
  } while (i < 1);
```

## Functions/Methods
 Functions are blocks of code that perform tasks and can be reused throughout a program. 
 They help in from having to repate code.

 Methods are functions that belong to a class. 
 They are used to define the behavior of objects created from the class.

### Arrays/Lists
 Arrays are a data structure that are used to store multiple values of similar data types.

### Matrices


 [Geeks For Geeks](https://www.geeksforgeeks.org/)

# aboudt 

## formating 

**Bold** 
*int* 

***italic***

bullet list:
* wwew

1. wefa
2. argeg


|------|


```C++

```