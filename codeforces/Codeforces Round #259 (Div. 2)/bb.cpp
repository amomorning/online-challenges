#include <stdio.h>
const int M = 2e5+10;
int a[M];

int main() {
	int n; scanf("%d", &n);
	for(int i = 0; i < n; i ++) scanf("%d", &a[i]);
	int cur = n-1;
	while(a[cur-1] <= a[cur] && cur) cur --;
	if(cur == 0) return puts("0"), 0;
	for(int i = 0; i < cur-1; i ++) if(a[i] > a[i+1]) 
		return puts("-1"), 0;
	if(a[n-1] > a[0]) return puts("-1"), 0;
	printf("%d\n", n-cur);
}
