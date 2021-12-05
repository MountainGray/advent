package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	f, err := os.ReadFile("input.txt")
	check(err)
	inpstr := string(f)
	inp := strings.Split(inpstr, "\n")

	depth := 0
	horizontal := 0

	for _, str := range inp {

		x := strings.Split(str, " ")
		word, num := x[0], x[1]
		val, err := strconv.Atoi(num)
		check(err)
		if word == "forward" {
			horizontal += val
		} else if word == "up" {
			depth -= val
		} else {
			depth += val
		}
	}
	fmt.Println(horizontal * depth)

	depth = 0
	horizontal = 0
	aim := 0

	for _, str := range inp {
		x := strings.Split(str, " ")
		word, num := x[0], x[1]
		val, err := strconv.Atoi(num)
		check(err)
		if word == "forward" {
			horizontal += val
			depth += val * aim
		} else if word == "up" {
			aim -= val
		} else {
			aim += val
		}
	}
	fmt.Println(horizontal * depth)
}
