package eulerUtil

import "math"

func IsPrime(n int) bool {

	if n < 0 {
		n = -n
	}

	if n == 0 || n == 1 || n == 2 || n == 3 {
		return true
	}

	i := 2
	ceil := int(math.Sqrt(float64(n)))
	for i <= ceil {
		if n%i == 0 {
			return false
		}
		i++
	}
	return true
}
