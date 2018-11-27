import Euler.Utils._

object P37 {
  def main(args: Array[String]) = {
    val range = 11 to args(0).toInt by 2
    val results = range
      .filter(i => i % 3 != 0)
      .map(a => a.toString)
       // digit 2,4,6,8,0,5 cannot exisit, unless the first digit
      .filter(a => !a.substring(1).exists(c => c % 2 == 0 || c == 53))
      .filter(a =>
        (a :: List.range(1, a.length)
          .map(i => a.substring(i) :: a.substring(0,i) :: Nil)
          .flatten)
        .map(s => s.toInt)
        .forall(i => isPrime(i)) // not exists non-prime <=> all prime
      )
      .map(s => s.toInt)


    println(results)
    println()
    println(results.map(s => s.toInt).sum)
  }
}
