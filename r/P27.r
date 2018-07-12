source('util.r')

getFunc <- function(a, b){
    f  <- function(n){
        return(n * n + a * n + b)
    }
    return(f)
}

numOfPrimes <- function(a, b){
    n = 0
    f = getFunc(a, b)
    while(isPrime(f(n))){
        n = n + 1
    }
    return(n)
}

goP27  <- function(){
    max = 0
    for(a in seq(-999, 999)){
        for(b in seq(-1000, 1000)){
            n = numOfPrimes(a, b)
            if(n <= max) next
            max = n
            print(sprintf("max: {%d}, a: {%d}, b: {%d}", max, a, b));
        }
    }
}

goP27()
