import scala.math._

object P44 {

  def main(args: Array[String]): Unit = {
    val u = 3000
    val l = (1 to u)
      .map(n => n * (3*n -1) /2)

    var d = 0
    for(d <- 1 to u){
      for(i <- 0 to (u - d - 1)){
        val p1 = l(i)
        val p2 = l(i+d)
        val s = p1 + p2
        if(isPtg(s)){
          val diff = p2 - p1
          if (isPtg(diff)) {
            println(s"D: $diff, i: $i, d:$d, p1: $p1, p2: $p2")
            return
          }
        }
      }
    }
    println("Not found")
  }

  def isPtg(n: Int) : Boolean = {
    val x = (sqrt(1 + 24 * n) + 1)/6.0
    return (x == x.toInt)
  }
}
