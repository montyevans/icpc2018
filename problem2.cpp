/*
Tightly Packed
*/
#include <iostream>
#include <cmath>
#include <limits>

using namespace std;

int main() {
  long N; cin >> N;

  long x = ceil(sqrt(N));
  long minDiff = numeric_limits<long>::max();

  while(true) {
    long y = ceil(N / (double) x);
    if(x > 2*y) break;

    int diff = x * y - N;
    if (diff < minDiff && diff >= 0) {
      minDiff = diff;
      if (minDiff == 0) break;
    }

    x++;
  }

  cout << minDiff << endl;
}
