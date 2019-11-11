package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	A, _ := strconv.Atoi(scanner.Text())

	scanner.Scan()
	C, _ := strconv.Atoi(scanner.Text())

	scanner.Scan()
	S, _ := strconv.Atoi(scanner.Text())

	scanner.Scan()
	X, _ := strconv.Atoi(scanner.Text())

	switch X {
	case 4:
		fmt.Println(S)
	case 5:
		fmt.Println(A)
	case 6:
		fmt.Println(C)
	}
}
