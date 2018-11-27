import scala.math._
import Euler.Utils._

object P52 {
  def main(args: Array[String]): Unit = {
    var notFound = true
    var i = 100000L
    while(notFound){
      if(ok(i)){
        notFound = false
        println(i)
      }
      i = i+1
    }
  }

  def ok(n: Long): Boolean = {
    val s = n.toString
    val t = s.toSet

    if(t.size < 6){
      return false
    }

    val l = s.length

    (2 to 6).forall(i => {
      val x = (i * n).toString
      x.length == l && x.toSet == t
    })
  }
}
