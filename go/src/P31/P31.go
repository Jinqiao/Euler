package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) == 1 {
		fmt.Printf("Please enter amount\n")
		return
	}

	// for i := 0; i < len(os.Args); i++ {
	//	fmt.Printf("%d: %s\n", i, os.Args[i])
	// }

	amount, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println(err)
		os.Exit(2)
	}

	fmt.Printf("result is %d\n", ways(amount, 7))
	return
}

var coins = [8]int{1, 2, 5, 10, 20, 50, 100, 200}

// t is target amount, i is current index in coins array(start from end)
func ways(t int, i int) int {
	if i <= 0 {
		return 1
	}

	r := 0
	for t >= 0 {
		r = r + ways(t, i-1)
		t = t - coins[i]
	}
	return r
}
