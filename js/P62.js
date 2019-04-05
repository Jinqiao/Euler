function print(s){
  process.stdout.write(s + "\n");
}

var m = {};
var i = 1;

while(true){
  i += 1;
  c = i * i * i;
  k = c.toString().split("").sort().join("");
  m[k] = (m[k] == undefined
          ? [c]
          : m[k].concat([c]));

  if(m[k].length == 5){
    m[k].forEach(a => print(a));
    break;
  }
}
