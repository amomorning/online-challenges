#include <bits/stdc++.h>
using namespace std;

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int n; scanf("%d", &n);
		int tot = n, m = n;
		for(int i = 2; 1ll*i*i <= n; ++ i)  {
			if(n%i == 0) {
				tot = 1ll*tot * (i-1)/i;
				while(n%i == 0) n /= i;
			}
		}
		if(n > 1) tot = 1ll*tot*(n-1)/n;
		printf("%lld\n" ,1ll*tot*(m-1));
	}
}
