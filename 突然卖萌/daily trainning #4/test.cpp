#include <bits/stdc++.h>
using namespace std;

int main(){
	int a[20];
	for(int i = 1; i <= 10; i ++) {
		a[i] = i;
	}
	int p = lower_bound(a+1, a+1+10, 29) - a;
	printf("%d\n", p);
}
