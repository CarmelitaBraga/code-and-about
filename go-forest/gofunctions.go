package main

import (
	"fmt"
	"os"
	"net/http"
)

func main() {
	welcome()
	menu()

	choice := choiceService()

	switch choice {
	case 1:
		monitor()
	case 2:
		fmt.Println("Logs...")
	case 0:
		fmt.Println("Exiting...")
		os.Exit(0)
	default:
		fmt.Println("This is not valid!")
		main()
	}

	os.Exit(0)
}

func welcome() {
	name := "Carmelita"
	fmt.Println(">>>Hey,", name, "\b. Welcome to MoniHTTPtoring!<<<")
}

func menu () {
	fmt.Println("Here's the provided services:")
	fmt.Println("1- Start monitoring")
	fmt.Println("2- Show logs")
	fmt.Println("0- Exit")
	fmt.Println("Choose an option:")
}

func choiceService() int {
	var choice int
	fmt.Scan(&choice)

	return choice
}

func monitor() {
	fmt.Println("Starting...")
	site := "https://www.louvre.fr/"
	response, _ := http.Get(site)
	fmt.Println(response)
}