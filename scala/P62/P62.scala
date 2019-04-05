import math._
import scala.collection.mutable.HashMap

object P62 {

  def main(args: Array[String]) = {
    val m = new HashMap[String, List[Long]]

    val l = Iterator.from(1)
      .map(_.toLong)
      .map(i => i * i * i)
      .map(c => {
        val k = c.toString.toList.sorted.mkString
        m(k) = if (m contains k)
          c :: m(k)
        else
          List(c)
        m(k)
      })
      .find(l => l.length == 5)
      .get

    println(l.sorted.mkString("\n"))

  }


  // Below is okay, but not functional
  // def main(args: Array[String]): Unit = {
  //   val m = new HashMap[String, List[Long]]
  //   var foundKey = ""
  //   var i = 1L
  //   while(foundKey == ""){
  //     val cube = i * i * i
  //     val key = cube.toString.toList.sorted.mkString
  //     if(m contains key){
  //       m(key) = cube.toLong :: m(key)
  //     }
  //     else{
  //       m(key) = List(cube.toLong)
  //     }
  //     if(m(key).length == 5){
  //       foundKey = key
  //     }
  //     i += 1
  //   }
  //   println(s"key = $foundKey")
  //   println(m(foundKey).sorted.mkString("\n"))
  // }

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
