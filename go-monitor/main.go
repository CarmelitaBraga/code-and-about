package main

import (
	"bufio"
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
	"time"
)

const filename = "go-monitor/websites.txt"
const logsfilename = "go-monitor/logs.txt"
const errorMsg = "An error has occurred:"
const numPings = 3
const delayTime = 10


func main() {
	welcome()

	for {
		menu()
		option := selectOption()

		switch option {
		case 1:
			fmt.Println("Monitoring...")
			sites := getSitesFromFile(filename)
			for i := 0; i < numPings; i ++ {
				for _, site := range(sites) {
					monitorSite(site)
				}

				time.Sleep(delayTime * time.Second)
			}
		case 2:
			fmt.Println("Logging...")
			showLogs()
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

	handleError(err)

	fmt.Println("Welcome to the Sites Monitor,", name, "\b!")
}

func menu() {
	fmt.Println("\n----------------Sites Monitor Options----------------")
	fmt.Println("1 - Monitor sites")
	fmt.Println("2 - Show logs")
	fmt.Println("0 - Exit system")
	fmt.Println("-----------------------------------------------------")
	fmt.Print("Option: ")
}

func selectOption() int {
	var opt int
	_, err := fmt.Scanf("%d", &opt)
	handleError(err)

	return opt
}

func getSitesFromFile(filename string) []string {
	file, err := os.Open(filename)
	handleError(err)

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
	handleError(err)

	active := false
	if statusCode == 200 {
		fmt.Println(site, "was successfully pinged!")
		active = true
	} else {
		fmt.Println("Something went wrong with the", site, 
					"\b. Status code:", statusCode, "\b.")
	}

	writeLogs(site, active)

}

func writeLogs(site string, active bool) {
	file, err := os.OpenFile(logsfilename, os.O_RDWR | os.O_CREATE | os.O_APPEND, 0666)

	handleError(err)
	var status string
	if active {
		status = "active"
	} else {
		status = "down"
	}

	timestamp := getCurrentTime()
	file.WriteString(timestamp + " the site " + site + " was " + status + ".\n")
	file.Close()
}

func showLogs() {
	file, err := os.ReadFile(logsfilename)
	handleError(err)

	fmt.Println(string(file))
}

func getCurrentTime() string {
	timestamp := time.Now().Format("2006-01-02 15:04:05")

	return timestamp
}

func handleError(err error) {
	if err != nil {
		fmt.Println(errorMsg, err)
	}
}