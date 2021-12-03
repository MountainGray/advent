package solution

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
	f, err := os.ReadFile("input.txt")
	check(err)
	inpstr := string(f)
	inp := strings.Split(inpstr, "\n")
	
	input = map()

}