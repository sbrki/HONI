package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func digitSum(x uint64) (sum uint64) {
	sum = 0
	for x > 0 {
		sum += x % 10
		x = x / 10
	}

	return sum
}

func digitCount(x uint64) (count uint64) {
	count = 0
	for x > 0 {
		count++
		x = x / 10
	}
	return count
}

func toSingleDigit(x uint64) (result uint64) {
	for {
		x = digitSum(x)
		c := digitCount(x)
		if c <= 1 {
			break
		}
	}
	return x
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	q, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < q; i++ {
		scanner.Scan()
		text := strings.Split(scanner.Text(), " ")
		var start, stop, sum uint64
		start, _ = strconv.ParseUint(text[0], 10, 64)
		stop, _ = strconv.ParseUint(text[1], 10, 64)

		for j := start; j <= stop; j++ {
			sum += toSingleDigit(j)
		}

		fmt.Println(sum)
	}
}
