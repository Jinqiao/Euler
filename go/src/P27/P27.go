package main

import (
	"eulerUtil"
	"fmt"
)

func main() {
	max := 0

	for a := -999; a < 1000; a++ {
		for b := -1000; b < 1001; b++ {
			n := NumP27Primes(a, b)
			if n <= max {
				continue
			}
			max = n
			fmt.Printf("max: {%d}, a: {%d}, b: {%d}\n", max, a, b)
		}
	}
}

func NumP27Primes(a, b int) int {
	n := 0
	for eulerUtil.IsPrime(n*n + a*n + b) {
		n++
	}
	return n
}
