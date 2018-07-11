// Check is a number is a prime
function isPrime(n){
  n = Math.abs(n);
  if(n in [0,1,2,3]) return true;
  var i = 2;
  ceil = Math.sqrt(n);
  while(i <= ceil){
    if(n%i == 0) return false;
    i++;
  }
  return true;
}

function getFunc(a, b){
  return function(n){
    return n * n + a * n + b;
  }
}

function numOfPrimes(a, b){
  n = 0;
  f = getFunc(a, b);
  while(isPrime(f(n))){
    n++;
  }
  return n;
}

// numOfPrimes(1, 41);

function print(s){
  process.stdout.write(s + "\n");
}

function solveP27(){
  var max = 0, A, B;
  for(var a = -999; a < 1000; a++){
    for(var b = -1000; b <= 1000; b++){
      var n = numOfPrimes(a, b);

      // if(n > 39) {
      //   print("n: " + n  + " a: " + a + " b: " + b);
      // }


      if(n > max) {
        max = n;
        A = a;
        B = b;
        print("n: " + n + " max: " + max + " A: " + A + " B: " + B);
      }
    }
  }
  return {a:A, b:B};
}

solveP27();
