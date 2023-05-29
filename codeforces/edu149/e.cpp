#include <bits/stdc++.h>
using LL = long long;

struct Solver {
 
  void solve(int ca, std::istream& reader) {
    int N, K;
    reader >> N >> K;
    std::vector<LL> A(N+1);
    for (int i = 0; i < N; ++ i) {
        reader >> A[i];
    }

    std::vector<LL> left(N+1);
    auto check = [&](LL bar) -> bool {
        std::priority_queue<LL> pq;
        LL s = 0;

        for(int i = 0; i < N; ++ i) {
            pq.emplace(A[i]);
            s += A[i];
            if (s > bar) {
                LL y = pq.top(); pq.pop();
                s -= y;
            }
            left[i+1] = pq.size();
        }

        while(!pq.empty()) pq.pop();
        s = 0;

        for (int i = N-1; i >= 0; -- i) {
            pq.emplace(A[i]);
            s += A[i];
            if (s > bar) {
                LL y = pq.top(); pq.pop();
                s -= y;
            }
            if (left[i] + pq.size() >= K) return true; 
        }
        return false;
    };

    LL l = 0, r = 1e18;
    LL ans = -1;
    while (l <= r) {
        LL m = (l+r) >> 1;
        if (check(m)) r = m-1;
        else l = m+1;
    }
    printf("%lld\n", r+1);
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
