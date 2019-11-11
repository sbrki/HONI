package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())

	sum := 0

	for i := 0; i < n; i++ {
		scanner.Scan()
		text := strings.Split(scanner.Text(), " ")
		filipSum, _ := strconv.Atoi(text[0] + text[1])
		sum += filipSum
	}

	fmt.Println(sum)
}
