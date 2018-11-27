package Euler

import scala.math._

object Utils {
  def getFactors(n: Int): List[Int] = {
    var x = abs(n)
    var i = 2
    var factors = List[Int]()
    val upBound = sqrt(n)
    while(i < upBound && x > 1) {
      while(x % i == 0){
        factors = i :: factors
        x /= i
      }
      i += 1
    }
    if(factors.isEmpty){
      factors = List(abs(n))
      x = 1
    }
    if (x > 1) {
      factors = x :: factors
    }
    return factors
  }

  def isPrime(a: Int): Boolean = {
    val n = if(a > 0) a else -a;
    if(n == 2 || n == 3 || n == 5 || n == 7)
      return true

    if(a % 2 == 0 || a % 3 == 0 || a % 5 == 0 || n == 0 || n == 1){
      return false
    }

    val ceil = sqrt(n).toInt
    return !(2 to ceil).exists(i => n % i == 0)
  }

  def numDigits(a: Int): Int ={
    var n = 1;
    var i = a;
    if ( i >= 100000000 ) { n += 8; i /= 100000000; }
    if ( i >= 10000     ) { n += 4; i /= 10000; }
    if ( i >= 100       ) { n += 2; i /= 100; }
    if ( i >= 10        ) { n += 1; }
    n
  }

  def gcd(a: Long, b: Long): Long = {
    if(b == 0) a else gcd(b, a % b)
  }
}
