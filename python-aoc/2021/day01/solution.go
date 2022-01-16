package main

import (
	"fmt"
	"os"
	"strings"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	data, err := os.ReadFile("input.txt")
	check(err)
	inputstring := string(data)
	inputstrings := strings.Split(inputstring, "\n")

	vals := make([]int, len(inputstrings))
	for index, b := range inputstrings{
		vals[index], err = strconv.Atoi(b)
		check(err)
	}
	var total int = 0
	for i := 1; i < len(vals) -1 ; i++ {
		if vals[i] < vals[i+1] {
			total++ 
		}
	}
	fmt.Println(total)

	total = 0
	for i := 1; i < len(vals) -3 ; i++ {
		if vals[i] < vals[i+3] {
			total++ 
		}
	}
	fmt.Println(total)
}