isPrime <- function(n){
    n  <-  abs(n)
    if(n %in% c(0,1,2,3)){
        return(TRUE)
    }
    i  <- 2
    ceil  <- sqrt(n)
    while(i <= ceil){
        if(n %% i == 0){
            return(FALSE)
        }
        i = i + 1
    }
    return(TRUE)
}
