import scala.math._
import Euler.Utils._

object P50 {
  def main(args: Array[String]): Unit = {
    val ps = (1 to 6999 by 2).filter(isPrime(_))
    val m = getUpperBound()
    println("m is " + m)
    for(i <- (m to 1 by -1)){
      val l = ps.sliding(i).map(_.sum).filter(_ < 1000000).filter(isPrime(_)).toList
      if(l.length >= 1){
        println(l)
        return
      }
    }
  }

  def getUpperBound(): Int = {
    var s = 10
    var i = 5
    var n = 2
    while(true){
      i += 2
      if(isPrime(i)){
        s += i
        n += 1
      }
      if(s >= 1000000){
        return n
      }
    }
    return 0
  }
}
