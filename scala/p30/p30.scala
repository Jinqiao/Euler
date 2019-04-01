import scala.math._

object P30 {
  def main(args: Array[String]) = {

    val r = List.range(2, args(0).toInt)
      // .collect {
      //   case e if e.toString.toList.map(c => pow(c.asDigit,5)).sum == e => e
      // }
      .filter(e => e.toString.toList.map(c => pow(c.asDigit,5)).sum == e)
      .sum

    println(r)
  }
}
