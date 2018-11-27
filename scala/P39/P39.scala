import scala.math._

object P39 {

  def main(args: Array[String]) : Unit = {
    val m = (120 to 1000)
      .map(p => (p, (1 to p/3)
        .map(a => getEdges(a, p - a)
          .map(l => l.sorted)
          .filter(k => pow(k(0), 2) + pow(k(1), 2) == pow(k(2), 2)))
        .filter(ll => ll.length > 0)
        .flatten
        .map(l => l.mkString("-"))
        .distinct
        .length
      ))
      .sortBy(p => p._2)
      .last
    println(m)
  }


  def getEdges(a: Int, bc: Int) = {
    var l = List[List[Int]]()
    var b = 0
    for(b <- (bc / 2) to (bc / 2 + a)){
      val c = bc - b
      val x = List(a, b, c)
      l = x :: l
    }
    l
  }
}
