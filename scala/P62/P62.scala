import math._
import scala.collection.mutable.HashMap

object P62 {

  def main(): Unit = {
    m = new HashMap[String, List[Long]]

    
  }

  // Bleow works, but too sloooow..
  // def main(args: Array[String]): Unit = {
  //   var num = 0
  //   var i = 1L
  //   while(num != 5){
  //     i += 1
  //     val cube = i * i * i
  //     val nD = cube.toString.length
  //     num = cube.toString.toList.permutations
  //       .map(l => l.mkString.toLong)
  //       .filter(l => l.toString.length == nD)
  //       .filter(n => isCube(n))
  //       .length
  //   }
  //   println(s"i = $i, cube = ${i * i * i}")
  // }

  // def isCube(n: Long): Boolean = {
  //   val x = round(cbrt(n))
  //   return x * x * x == n
  // }
}
