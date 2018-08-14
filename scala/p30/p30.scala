import scala.math._

object P30 {
  def main(args: Array[String]) = {

    // collect is slightly faster than the following map
    val r = List.range(2, args(0).toInt)
      .collect {
        case e if e.toString.toList.map(c => pow(c.asDigit,5)).sum == e => e
      }
      .sum

    // val r = List.range(2, args(0).toInt).map(e => {
    //       val ss = e.toString.toList.map(c => pow(c.asDigit,5)).sum
    //   if (ss == e)
    //     e
    //   else
    //     0
    // }).sum

    println(r)
  }
}
