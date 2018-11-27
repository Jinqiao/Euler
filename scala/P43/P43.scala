object P43 {

  val primes = List(2,3,5,7,11,13,17)

  def main(args: Array[String]): Unit = {
    val r = (0 to 9).toList.permutations
      .filter(l => l(0) != 0)
      .map(l => l.mkString)
      .filter(s => isSubStrDiv(s))
      .toList

    println(r.mkString("\n"))
    println("sum: " + r.map(s => s.toLong).sum.toString)
  }

  def isSubStrDiv(s: String): Boolean = {
    val n = s.toLong
    var i = 0

    for(i <- 1 to 7) {
      val d = s.substring(i, i + 3).toInt
      if(d % primes(i-1) != 0){
        return false
      }
    }

    return true
  }
}
