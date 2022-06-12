#include <bits/stdc++.h>
using namespace std;

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		int a, b, c, d;
		scanf("%d%d%d%d", &a, &b, &c, &d);
		if(a+c > b+d) puts("1");
		else if(a+c < b+d) puts("2");
		else {
			if(b>c) puts("2");
			else if(c>b) puts("1");
			else puts("-1");
		}
	}
}
