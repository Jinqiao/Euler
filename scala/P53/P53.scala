import scala.math._
import Euler.Utils._

object P53 {
  def main(args: Array[String]): Unit = {
    var i = 0
    for(
      n <- 23 to 100;
      r <- 2 to n / 2
      if ok(n, r)
    ){
      i = i + (if(r == n/2 && n % 2 == 0) 1 else 2)
    }
    println(i)
  }

  def ok(n: Int, r: Int): Boolean = {
    val uList = (n to 1 by -1).toList
    val s = n - r
    val dList = (min(r, s) to 1 by -1).toList ::: (max(r, s) to 1 by -1).toList

    val vList = (uList zip dList)
      .takeWhile(p => p._1 != p._2)
      .map(p => 1.0 * p._1 / p._2)

    var x = 1.0

    for(v <- vList){
      x = x * v
      if(x > 1000000){
        return true
      }
    }

    if(x > 1000000){
      return true
    }

    return false
  }

  def max(a: Int, b: Int): Int = {
    if(a > b) a else b
  }

  def min(a: Int, b: Int): Int = {
    if(a < b) a else b
  }
}
