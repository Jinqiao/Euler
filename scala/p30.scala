import scala.math._

object P30 {
  def main(args: Array[String]) = {

    val r = List.range(2, args(0).toInt).map(e => {
      // if a element satisfies the requirement then returns it,
      // otherwise returns 0
      val ss = e.toString.toList.map(c => pow(c.asDigit,5)).sum
      if (ss == e)
        e
      else
        0
    }).sum

    println(r)
  }
}
