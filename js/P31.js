coins = [1, 2, 5, 10, 20, 50, 100, 200];
amount = 200;

// t is target amount, i is current index in coins array(start from end)
function ways(t, i){
  if(i <= 0 || t == 0) return 1;

  res = 0;
  while(t >= 0){
    res = res + ways(t, i - 1);
    t = t - coins[i];
  }
  return res;
}


function print(s){
  process.stdout.write(s + "\n");
}


print(ways(amount, 7));
