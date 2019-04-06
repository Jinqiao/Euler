#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

int main()
{
  map<string, vector<long> > m;
  long long i = 1, c = 0;
  string k;

  while (true) {
    i += 1;
    c = i * i * i;
    k = to_string(c);
    sort(k.begin(), k.end());
    auto iter = m.find(k);

    if (iter == m.end()) {
      vector<long> v;
      v.push_back(c);
      m[k] = v;
    }
    else {
      auto v0 = iter->second;
      v0.push_back(c);
      m[k] = v0; // this line is needed!

      if(v0.size() == 5){
        for (int j = 0; j < 5; ++j) {
          cout << "k = " << k << " c = " << v0[j] << endl;
        }
        break;
      }
    }

  }

  return 0;
}
