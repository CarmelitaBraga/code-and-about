package main

import "fmt"

func main() {
	fmt.Println("Hello, world!")

	var nome string = "Carmelita Braga"
	var idade int = 23
	var altura float32

	fmt.Println("Hi, my name is", nome, "and I'm", idade, "years old.")
	fmt.Println("My height is", altura)

	// var message string
	// fmt.Scanf("%s", &message)
	// fmt.Println(message)

	fmt.Printf("%c\n", nome[1])
	s := "hello"
	fmt.Println(s[0])          // Output: 104 (ASCII value of 'h')
	fmt.Printf("%c\n", s[0])   // Output: h

	runes := []rune(s)
	fmt.Println(string(runes))

}