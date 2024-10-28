package main

import (
	"bufio"
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
)

const filename = "go-monitor/websites.txt"
const errorMsg = "An error has occurred:"

func main() {
	welcome()

	for {
		menu()
		option := selectOption()

		switch option {
		case 1:
			fmt.Println("Monitoring...")
			sites := getSitesFromFile(filename)
			fmt.Println(sites)
			for _, site := range(sites) {
				monitorSite(site)
			}
		case 2:
			fmt.Println("Logging...")
		case 0:
			fmt.Println("Exiting...")
			os.Exit(0)
		default:
			fmt.Println("Invalid option!")
		}
	}
}

func welcome() {
	fmt.Print("Type your name: ")

	var name string
	_, err := fmt.Scan(&name)

	if err != nil {
		fmt.Println(errorMsg, err)
	}


	fmt.Println("Welcome to the Sites Monitor,", name, "\b!")
}

func menu() {
	fmt.Println("\n----------------Sites Monitor Options----------------")
	fmt.Println("1 - Monitor sites")
	fmt.Println("2 - Show logs")
	fmt.Println("0 - Exit system")
	fmt.Println("-----------------------------------------------------")
	fmt.Println()
}

func selectOption() int {
	var opt int
	_, err := fmt.Scanf("%d", &opt)

	if err != nil {
		fmt.Println(errorMsg, err)
	}

	return opt
}

func getSitesFromFile(filename string) []string {
	file, err := os.Open(filename)

	if err != nil {
		fmt.Println(errorMsg, err)
	}

	sites := []string{}
	reader := bufio.NewReader(file)

	for {
		line, err := reader.ReadString('\n')
		line = strings.TrimSpace(line)
		sites = append(sites, line)

		if err == io.EOF {
			break
		}
	}

	return sites
}

func monitorSite(site string) {
	resp, err := http.Get(site)
	statusCode := resp.StatusCode

	if err != nil {
		fmt.Println(errorMsg, err)
	}

	if statusCode == 200 {
		fmt.Println(site, "was successfully pinged!")
	} else {
		fmt.Println("Something went wrong with the", site, 
					"\b. Status code:", statusCode, "\b.")
	}
}