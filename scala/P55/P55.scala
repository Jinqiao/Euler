import scala.math._
import Euler.Utils._

object P55 {
  def main(args: Array[String]): Unit = {
    val r = (1 to 9999).map(i => if(isLychrel(i)) 1 else 0).sum
    println(r)
  }

  def sum(s1: String, s2: String): String = {
    val L = if(s1.length > s2.length) s1.length else s2.length;
    val d1 = s1.reverse.map(c => c.toInt - 48).padTo(L, 0)
    val d2 = s2.reverse.map(c => c.toInt - 48).padTo(L, 0)

    val h = (d1 zip d2).map(p => (p._1 + p._2, ""))
      .reduceLeft((x, y) => (x._1 / 10 + y._1, x._1 % 10 + x._2))

    h._1 + h._2
  }

  def isPalindrome(s: String): Boolean = {
    (0 to (s.length - 1)).forall(i => s(i) == s(s.length - i -1))
  }

  def getNext(s: String): String = {
    sum(s, s.reverse)
  }

  def isLychrel(n: Int): Boolean = {
    var s = n.toString
    for(i <- 1 to 50) {
      s = getNext(s)
      if(isPalindrome(s)){
        return false
      }
    }
    true
  }
}
