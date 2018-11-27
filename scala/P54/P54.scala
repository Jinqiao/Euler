import scala.math._
import Euler.Utils._
import scala.io.Source

object P54 {
  def main(args: Array[String]): Unit = {
    val f = "p054_poker.txt"
    val r = Source.fromFile(f).getLines.map(l => l.split(' ').splitAt(5))
      .map(hh => isFirstHandWin(hh._1, hh._2))
      .count(b => b)

    println(r)
  }

  def isFirstHandWin(p: Array[String], q: Array[String]): Boolean = {
    val pL = getHandLevel(p)
    val qL = getHandLevel(q)
    var r = true
    if(pL > qL){
      r = true
    }
    else if(pL < qL){
      r = false
    }
    else {
      val pS = getSortedHand(p)
      val qS = getSortedHand(q)
      val x = (pS zip qS).map(k => k._1 - k._2)
        .filter(_ != 0)
        .head
      r = x > 0
    }

    // println(p.mkString(" ") + " <-> " + q.mkString(" ") + " : " + r)

    r
  }

  def getSortedHand(h: Array[String]): List[Int] = {
    h.map(d => toCardNumber(d(0), h))
      .groupBy(a => a)
      .toList
      .sortBy(t => -100 * t._2.size - t._2(0))
      .map(_._2)
      .flatten
  }

  def getHandLevel(h: Array[String]): Int = {
    val tongHua = isTongHua(h)
    val shun = isShunZi(h)

    if(tongHua){
      if(shun) return 9
      else return 6
    }
    if(shun) return 5

    val strPattern = h.groupBy(d => d(0))
      .mapValues(_.size)
      .map(_._2)
      .toList
      .sortBy(-1 * _)
      .mkString

    strPattern match {
      case "11111" => 1
      case "2111" => 2
      case "221" => 3
      case "311" => 4
      case "32" => 7
      case "41" => 8
    }
  }

  def isTongHua(h: Array[String]): Boolean = {
    val c1 = h(0)(0)
    h.forall(d => d(0) == c1)
  }

  def isShunZi(h: Array[String]): Boolean = {
    h.map(d => toCardNumber(d(0), h))
      .sorted
      .sliding(2)
      .forall(l => l(1) - l(0) == 1)
  }

  def toCardNumber(c: Char, h: Array[String]): Int = {
    val i = c.toInt
    if(i < 58){
      return i - 48
    }

    c match {
      case 'T' => 10
      case 'J' => 11
      case 'Q' => 12
      case 'K' => 13
      case 'A' => {
        if(h.map(_(0)).sorted.mkString == "2345A") {
          println(h)
          1
        } else 14
      }
    }
  }
}
