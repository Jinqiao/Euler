import scala.collection.mutable
import Euler.Utils._
import scala.math._

object P32 {
  def main(args: Array[String]) = {
    val r = List.range(1002, 9999).filter(isPandigitalProd).sum
    println(r)
  }

  def getSubsets(s: List[Int]):List[List[Int]] = {
    val n = s.length
    List.range(1, 1<< n).map(i => {
      List.range(0, n)
        .filter(j => (i & (1 << j)) > 0)
        .map(j => s(j))
    })
  }

  def split(n: Int) = {
    getSubsets(getFactors(n))
      .map(s => s.reduceLeft(_ * _))
      .map(i => {
        val n2 = n / i
        (min(i, n2), max(i, n2))
      })
      .distinct
  }

  def isPandigitalProd(n: Int): Boolean = {
    val nStr = n.toString
    split(n).exists(pair => {
      val s = nStr + pair._1.toString + pair._2.toString
      s.length == 9 && !(s contains '0') && s.toSet.size == 9
    })
  }
}
