package main

import "fmt"
import "os"

func main() {
	name := "Carmelita"
	fmt.Println("Hi,", name, "\b. Are you ready for another lession?")

	fmt.Println("2- Planejar as férias")
	fmt.Println("5- Ler & anotar")
	fmt.Println("7- Jogar um pouco")
	fmt.Println("0- Descansar")

	var command int
	fmt.Scanf("%d", &command)
	
	fmt.Println("You have chosen option:", command)
	fmt.Println("Variable address is:", &command)

	var answer string
	fmt.Print("Tell us how you're going to do that: ")
	fmt.Scanln(&answer)
	fmt.Println("Cool! I see that you're going", answer)

	s := "Fletcher"
	sub := s[1:5]
	fmt.Println(sub)

	if command == 2 {
		fmt.Println("You go plan, girl!")
	} else if command == 5 {
		fmt.Println("You go plan, girl!")
	} else if command == 7 {
		fmt.Println("You go play, girl!")
	} else if command == 0 {
		fmt.Println("You go rest, girl!")
	} else {
		fmt.Println("Go do something else then! :D")
	}

	fmt.Println("Le numéro est le suivant :")
	switch command {
	case 5:
		fmt.Println("Cinque")
	case 2:
		fmt.Println("Deux")
	case 7:
		fmt.Println("Sept")
	case 0:
		fmt.Println("Zèro")	
	default:
		fmt.Println("Saisissez un numéro valide, alors.")	
	}

	os.Exit(0)
}