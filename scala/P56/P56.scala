import java.math._
import scala.math._

object P56 {
  def main(args: Array[String]): Unit = {
    val r = (2 to 99).flatMap(x => (2 to 100).map(y => getPower(x, y)))
      .map(digitSum(_))
      .max

    println(r)
  }

  def digitSum(n: BigInteger): Int = {
    n.toString.map(c => c - 48).sum
  }

  def getPower(a: Int, b: Int): BigInteger = {
    (1 to a).map(x => new BigInteger(b.toString))
      .reduce((l, r) => l.multiply(r))
  }
}
