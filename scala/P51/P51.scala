import scala.math._
import Euler.Utils._

object P51 {
  def main(args: Array[String]): Unit = {
    val primes = (100001 to 999999 by 2).filter(isPrime(_)).toList
    val indexList2 = (0 to 4).combinations(3).toList
    val r = primes
      .flatMap(n => indexList2.map(v => getMaskString(v, n)))
      .groupBy(x => x)
      .filter(_._1 != "")
      .filter(_._2.length >= 8)

    r.take(10).foreach(println(_))
    // println(r)
  }

  def getMaskString(v: IndexedSeq[Int], n: Int): String = {
    val a = n.toString.toArray
    if(v.forall(i => a(i) == a(v(0)))){
      v.foreach(i => a(i) = '*')
      return a.mkString
    }
    return ""
  }
}
