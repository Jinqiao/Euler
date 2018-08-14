object P31 {

  val coins = Array(1, 2, 5, 10, 20, 50, 100, 200);

  def main(args: Array[String]) = {
    val amount = args(0).toInt
    println(s"Total number of hands: ${ways(amount, 7)}")
  }


  def ways(t: Int, i: Int):Int = {
    if (i <= 0) {
      return 1
    }

    var r = 0
    var tt = t
    while(tt >= 0){
      r = r + ways(tt, i - 1)
      tt = tt - coins(i)
    }
    return r
  }
}
