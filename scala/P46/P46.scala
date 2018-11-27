import scala.math._

object P46 {

  def main(args: Array[String]): Unit = {
    var i = 5
    while(true){
      i += 2

      if(!isPrime(i) && !canSplit(i)){
        println(i)
        return
      }
    }
  }

  var primes = List(5, 3, 2, 1)


  def isPrime(n: Int): Boolean = {
    for(x <- primes.filter(k => k * k <= n && k > 1)){
      if(n % x == 0){
        return false
      }
    }

    primes = n :: primes
    // println(n)
    return true
  }


  def canSplit(n: Int): Boolean = {
    for(p <- primes){
      val sp = sqrt((n - p) / 2)
      if(sp == sp.toInt){
        return true
      }
    }

    return false
  }
}
