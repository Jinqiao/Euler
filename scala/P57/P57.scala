import scala.math._
import Euler.Utils._

object P57 {
  def main(args: Array[String]): Unit = {
    var x = (BigInt("2"), BigInt("1"))
    var n = 0
    for(i <- 1 to 1000){
      x = next(x._1, x._2)
      if(isNumeratorMoreDigits(x._2, x._1)){
        n = n + 1
      }
    }
    println(n)
  }

  def next(n: BigInt, d: BigInt): (BigInt, BigInt) = {
    val n2 = n * 2 + d
    val d2 = n
    (n2, d2)
  }

  def isNumeratorMoreDigits(n: BigInt, d: BigInt): Boolean = {
    (n + d).toString.length > d.toString.length
  }
}
