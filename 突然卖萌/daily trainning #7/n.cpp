#include <bits/stdc++.h>
int k, p, x;

double get(int m) {
	return 1.0*k/m*p+x*m;
}

int main() {
	scanf("%d%d%d", &k, &p, &x);
	int m = sqrt(1.0*k*p/x);
	printf("%.3lf\n", std::min(get(m), get(m+1)));
}
