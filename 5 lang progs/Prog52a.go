package main

import (
  "fmt"
  
)

func main() {
	fmt.Print("Enter length: ")
	var length int
	fmt.Scanln(&length)

	fmt.Print("Enter something: ")
	var width int
	fmt.Scanln(&width)
	var perimeter = 2 * (length + width)
	var area  = length * width 
    var A = fmt.Sprint(area)
	var P = fmt.Sprint(perimeter)
	fmt.Println("The area is ", A )
	fmt.Println("The width is " , P)

/*
Enter length: 2
Enter something: 2
The area is  4
The width is  8
/*
