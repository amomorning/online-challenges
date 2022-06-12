#include <bits/stdc++.h>

int main() {
	int m, n;
    scanf("%d%d", &m, &n);
	double ans = 0;
	for(int i = 1; i <= m; i ++) {
		double tmp = pow(1.0*i/m, n) - pow(1.0*(i-1)/m, n);
		ans += tmp*i;
	}
    printf("%.12f", ans);
}
