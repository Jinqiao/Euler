import scala.math._
import Euler.Utils._

object P47 {

  def main(args: Array[String]): Unit = {
    var i = 650
    factorMap += (i-1 -> getFactors(i-1).toSet)
    factorMap += (i-2 -> getFactors(i-2).toSet)
    factorMap += (i-3 -> getFactors(i-3).toSet)
    while(true){
      factorMap += (i -> getFactors(i).toSet)
      if(has4FactorsAll(i, i-1, i-2, i-3)){
        println(i-3)
        return
      }

      i += 1
    }
  }

  val factorMap = collection.mutable.Map[Int, Set[Int]]()

  def has4FactorsAll(n1: Int, n2: Int, n3: Int, n4: Int): Boolean = {
    val f1 = factorMap(n1)
    if(f1.size != 4) return false

    val f2 = factorMap(n2)
    if(f2.size != 4) return false

    val f3 = factorMap(n3)
    if(f3.size != 4) return false

    val f4 = factorMap(n4)
    return f4.size == 4
  }

}
