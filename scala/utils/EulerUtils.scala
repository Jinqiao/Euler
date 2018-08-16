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
}
