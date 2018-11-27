import scala.math._
import Euler.Utils._

object P58 {
  def main(args: Array[String]): Unit = {
    while(1.0 * NP / N > 0.1 || NP == 0){
      next()
    }
    println(L+1)
  }

  var L = 2;
  var X = 1;
  var C = 0;
  var N = 1;
  var NP = 0;

  def next() = {
    if(C < 4){
      C = C + 1
    }
    else if(C == 4){
      C = 1
      L = L + 2
    }
    X = X + L
    N = N + 1

    if(isPrime(X)){
      NP = NP + 1
    }
  }
}
