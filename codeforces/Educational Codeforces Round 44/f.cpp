#include <bits/stdc++.h>
const int N = 2e5+10;
int t;
int n, m;
char s[N];

int L[N], R[N], pos[N];
bool vis[N][30];
std::set<int> st[N];

int get(int l, int r, int a[]){
	for(int i = 0; i < 26; ++ i) a[i] = 0;
	int p = pos[l], q = pos[r];
	if(p == q) {
		for(int i = l; i <= r; ++ i) {
			a[s[i]-'a'] ++;
		}
	} else {
		for(int i = p+1; i < q; ++ i) {
			tmp.insert(st[i].begin(), st[i].end());
		}
		for(int i = l; i <= R[p]; ++ i) tmp.insert(s[i]);
		for(int i = L[q]; i <= r; ++ i) tmp.insert(s[i]);
	}
	return tmp.size();
}

int main(){
	scanf("%d%d%s", &n, &m, s+1);
	t = sqrt(n);
	for(int i = 1; i <= t; ++ i) {
		L[i] = (i-1)*t + 1;
		R[i] = i*t;
	}
	if(R[t] < n) t ++, L[t] = R[t-1]+1, R[t] = n;

	for(int i = 1; i <= t; ++ i) {
		for(int j = L[i]; j <= R[i]; j ++) {
			pos[j] = i;
			st[i].insert(s[j]);
		}
	}

	while(m --){
		int x, y, l;
		scanf("%d%d%d", &x, &y, &l);
		if(get(x, x+l-1) == get(y, y+l-1)) {
			puts("YES");
		} else {
			puts("NO");
		}
	}
}
