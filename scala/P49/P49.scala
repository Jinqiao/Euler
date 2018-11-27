import scala.math._
import Euler.Utils._

object P49 {

  def main(args: Array[String]): Unit = {
    val l = (1001 to 9999 by 2)
      .filter(a => isPrime(a))
      .groupBy(_.toString.sorted)
      .map(_._2.sorted.toList)
      .filter(_.length >= 3)
      .map(_.combinations(3))
      .flatten
      .map(_.sorted)
      .filter(s => s(1) - s(0) == s(2) - s(1))
      .foreach{
        println
      }
  }

  def isArithmeticProg(l: List[Int]): Boolean = {
    val d = l(1) - l(0)
    return l.sliding(2).forall(a => a(1) - a(0) == d)
  }
}
