#include <string>
#include <vector>
#include <iostream>
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



namespace power_details {
template<typename T, typename Enable = void>
struct Identity { static constexpr T get() { return T{1}; } };
template<typename T>
struct Identity<T, std::void_t<decltype(T::identity())>> {
  static constexpr T get() { return T::identity(); }
};
}  // namespace power_details

template<typename T,
         typename MulFunc = std::function<T(T,T)>,
         typename SqrFunc = std::function<T(T)>>
constexpr T power(T a, long long b, MulFunc&& mul, SqrFunc&& sqr) {
  T ret = sqr(power_details::Identity<T>::get());
  for (; b; b >>= 1, a = sqr(a)) if (b & 1) ret = mul(ret, a);
  return ret;
}
template<typename T, typename MulFunc = std::function<T(T,T)>>
constexpr T power(T a, long long b, MulFunc&& mul) {
  return power(a, b, std::forward<MulFunc>(mul), [&](T x) { return mul(x, x); });
}
template<typename T, typename IT = T>
constexpr T power(T a, long long b, T mod) {
  return power(a, b, [&mod](T x, T y) { return static_cast<IT>(x) * y % mod; });
}
template<typename T>
constexpr T power(T a, long long b) {
  return power(a, b, [](T x, T y) { return x * y; });
}

template<typename T>
struct PowerTable final : public std::vector<T> {
  PowerTable() = default;
  PowerTable(int n, const T& g)
    : PowerTable(n, g, [](const T& lhs, const T& rhs) -> T { return lhs * rhs; }) {}
  template<typename MulFunc = std::function<T(T,T)>>
  PowerTable(int n, const T& g, MulFunc&& mul) {
    static_assert(sizeof(PowerTable) == sizeof(std::vector<T>), "");
    this->resize(n + 1);
    this->at(0) = power_details::Identity<T>::get();
    for (int i = 1; i < this->size(); ++i) this->at(i) = mul(this->at(i - 1), g);
  }
};

// PowerTable<Mint> pw2(200000, 2);

//-#include "power.hpp"




template<typename T>
T gcd(T a, T b) {
  // NOTE: In case T is a polynomial,
  // no guartee that the result is a monic polynomial,
  // do an extra division if needed.
  return b == T{} ? a : gcd(b, a % b);
}

template<typename T>
T exgcd(T a, T b, T& x, T& y) {
  // NOTE: In case T is a polynomial,
  // no guartee that the result is a monic polynomial,
  // do an extra division if needed.
  if (b == T{}) return x = T{1}, y = T{}, a;
  T g = exgcd(b, a % b, y, x);
  y -= a / b * x;
  return g;
}

template<typename T>
T inv_coprime(T a, T n) {
  T x, y;
  assert(exgcd(a, n, x, y) == T{1});
  return (x % n + n) % n;
}

//-#include "exgcd.hpp"


// a * x + b * y == c
// g = |gcd(a, b)|
// |x|, |y| <= max(|a|, |b|, |c|)
//
// General solution:
//   xx = x + b / g * t
//   yy = y - a / g * t
//   for all t in Z
template<typename T = long long>
bool diophantine(T a, T b, T c, T& x, T& y, T& g) {
  if (a == 0 && b == 0) return c == 0 ? (x = y = g = 0, true) : false;
  if (a == 0) return (c % b == 0) ? (x = 0, y = c / b, g = std::abs(b), true) : false;
  if (b == 0) return (c % a == 0) ? (x = c / a, y = 0, g = std::abs(a), true) : false;
  g = exgcd(a, b, x, y);
  if (c % g != 0) return false;
  T dx = c / a;
  c -= dx * a;
  T dy = c / b;
  c -= dy * b;
  x = dx + (T)((__int128)x * (c / g) % b);
  y = dy + (T)((__int128)y * (c / g) % a);
  g = std::abs(g);
  return true;
}

//-#include "diophantine.hpp"


// Chinese remainder theorem
template<typename T = long long>
bool crt(T k1, T m1, T k2, T m2, T& k, T& m) {
  k1 %= m1;
  if (k1 < 0) k1 += m1;
  k2 %= m2;
  if (k2 < 0) k2 += m2;
  T x, y, g;
  if (!diophantine<T>(m1, -m2, k2 - k1, x, y, g)) return false;
  T dx = m2 / g;
  T delta = x / dx - (x % dx < 0);
  k = m1 * (x - dx * delta) + k1;
  m = m1 / g * m2;
  assert(0 <= k && k < m);
  return true;
}

//-#include "crt.hpp"


struct PrimeTable {
  std::vector<int> primes;
  std::vector<int> min_div;

  PrimeTable() = default;
  explicit PrimeTable(int n) { make(n); }

  void make(int n) {
    if (n < 1) return;
    primes.clear();
    min_div.assign(n + 1, 0);
    min_div[1] = 1;
    for (int i = 2; i <= n; ++i) {
      if (!min_div[i]) {
        primes.emplace_back(i);
        min_div[i] = i;
      }
      for (int p : primes) {
        if (i * p > n) break;
        min_div[i * p] = p;
        if (i % p == 0) break;
      }
    }
  }

  template<typename T>
  bool is_prime(T x) const {
    if (x < 2) return false;
    if (x < min_div.size()) return min_div[x] == x;
    for (int p : primes) {
      if (p * 1LL * p > x) break;
      if (x % p == 0) return false;
    }
    for (T w = std::max<T>(2, min_div.size()); w * 1LL * w <= x; ++w) {
      if (x % w == 0) return false;
    }
    return true;
  }

  template<typename T>
  std::vector<typename std::pair<T, T>> get_canonical_representation(T x) const {
    assert(x >= 1);
    std::vector<typename std::pair<T, T>> ret;  // <prime, cnt>
    for (int p : primes) {
      if (p * 1LL * p > x) break;
      if (x < min_div.size()) break;
      if (x % p == 0) {
        T cnt = 0;
        while (x % p == 0) ++cnt, x /= p;
        ret.emplace_back(p, cnt);
      }
    }
    for (T i = min_div.size(); x >= min_div.size() && i * 1LL * i <= x; ++i) if (x % i == 0) {
      T cnt = 0;
      while (x % i == 0) ++cnt, x /= i;
      ret.emplace_back(i, cnt);
    }
    while (1 < x && x < min_div.size()) {
      T p = min_div[x];
      T cnt = 0;
      while (x % p == 0) ++cnt, x /= p;
      ret.emplace_back(p, cnt);
    }
    if (x >= min_div.size() && x > 1) {
      ret.emplace_back(x, 1);
    }
    return ret;
  }

  template<typename T>
  std::vector<T> get_factors(T x) const {  // Note: Not in ascending order.
    assert(x >= 1);
    const std::vector<typename std::pair<T, T>> repr = get_canonical_representation(x);
    std::vector<T> factors;
    auto rec = [&](auto self, int at, T val) -> void {
      factors.emplace_back(val);
      for (int i = at; i < repr.size(); ++i) {
        T tmp = val;
        for (int j = 0; j < repr[i].second; ++j) {
          tmp *= repr[i].first;
          self(self, i + 1, tmp);
        }
      }
    };
    rec(rec, 0, 1);
    return factors;
  }

  template<typename T>
  std::vector<T> get_factors_with_nonzero_mu(T x) const {  // Note: Not in ascending order.
    assert(x >= 1);
    const std::vector<typename std::pair<T, T>> repr = get_canonical_representation(x);
    std::vector<T> factors;
    auto rec = [&](auto self, int at, T val) -> void {
      factors.emplace_back(val);
      for (int i = at; i < repr.size(); ++i) {
        self(self, i + 1, val * repr[i].first);
      }
    };
    rec(rec, 0, 1);
    return factors;
  }
};

//-#include "prime_table.hpp"

PrimeTable pt(100000);

struct Solver {

  void solve(int ca, std::istream& reader) {
    LL A, X, M;
    reader >> A >> X >> M;

    LL e = 0, w = 1;
    for (const auto& [p, b] : pt.get_canonical_representation(M)) {
      assert(crt(e, w, calc(A, X, p, b), power(p, b), e, w));
    }
    printf("%lld\n", e);
  }

  LL calc(LL A, LL X, LL p, LL b) {
    LL M = power(p, b);
    if (M == 1) return 0;
    if (A == 1) return X % M;
    if (A % M == 0) return 1;
    if (gcd(A - 1, M) == 1) {
      return (power(A, X, M) + M - 1) % M * inv_coprime(A - 1, M) % M;
    }
    LL t = 0;
    LL a = A - 1;
    while (a % p == 0) a /= p, ++t;
    using i128 = __int128_t;
    i128 mm = power(p, t) * i128{M};
    LL tmp = (power<i128>(A, X, mm) + mm - 1) % mm / power(p, t);
    return tmp * inv_coprime(a, M) % M;
  }
};

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::istream& reader = std::cin;

  int cas = 1;
  // reader >> cas;
  for (int ca = 1; ca <= cas; ++ca) {
    auto solver = std::make_unique<Solver>();
    solver->solve(ca, reader);
  }
}

