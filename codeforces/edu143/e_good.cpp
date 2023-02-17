#include <string>
#include <vector>
#include <iostream>
#include <numeric>
#ifdef ALGO
#include "el_psy_congroo.hpp"
#else
#define CHECK(...)
#define DUMP(...)
#define TIMER(...)
#endif

using LL = long long;
template<typename T, typename U>
inline bool enlarge(T& a, U b) { return a < b ? (a = b, true) : false; }
template<typename T, typename U>
inline bool minify(T& a, U b) { return a > b ? (a = b, true) : false; }


struct Boom {

  void append(int h) {
    int l1 = 1, h1 = h;
    while (!stack.empty() && stack.back().second > h1 - l1) {
      auto [l0, h0] = stack.back(); stack.pop_back();
      sum -= (h0 + h0 - l0 + 1) * 1LL * l0 / 2;
      l1 += l0;
    }
    minify(l1, h1);
    sum += (h1 + h1 - l1 + 1) * 1LL * l1 / 2;
    stack.emplace_back(l1, h1);
  }

  LL sum = 0;
  std::vector<std::pair<int, int>> stack;  // <len, r>, means l=r-len+1, l+1, l+2, .., r
};

struct Solver {

  void solve(int ca, std::istream& reader) {
    int N;
    reader >> N;

    std::vector<int> H(N);
    for (int i = 0; i < N; ++i) {
      reader >> H[i];
    }

    std::vector<LL> f(N);

    {
      Boom boom;
      for (int i = 0; i < N; ++i) {
        boom.append(H[i]);
        f[i] += boom.sum - H[i];
      }
    }
    {
      Boom boom;
      for (int i = N - 1; i >= 0; --i) {
        boom.append(H[i]);
        f[i] += boom.sum - H[i];
      }
    }

    LL result = std::accumulate(H.begin(), H.end(), 0LL) -\
                *std::max_element(f.begin(), f.end());
    printf("%lld\n", result);
  }
};

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::istream& reader = std::cin;

  int cas = 1;
  reader >> cas;
  for (int ca = 1; ca <= cas; ++ca) {
    auto solver = std::make_unique<Solver>();
    solver->solve(ca, reader);
  }
}

