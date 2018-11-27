object P38 {
  def main(args: Array[String]) : Unit = {
    (99999 to 1 by -1).find(isPandigitalMultiple);
  }

  def isPandigitalMultiple(n: Int) : Boolean = {
    var a = ""
    for(i <- 1 to 9){
      val x = i * n
      a += x
      if(a.exists(c => c == 48)){
        return false
      }
      if(a.length != a.distinct.length){
        return false
      }
      else if(a.length == 9 && i > 1){
        println(a)
        return true
      }
    }
    return false
  }
}
