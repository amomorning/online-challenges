#include <bits/stdc++.h>
const int M = 110;

int e[M][M], a[M][M], d[M][M];
int n, m;

bool check(int u, int v, int ls, int o) {
	if(o) {
		for(int i = 0; i < n; i ++) {
			if(e[v][i] > ls) return false;
		}
	} else {
		for(int i = 0; i < n; i ++) {
			if(e[u][i] > ls) return false;
		}
	}
	return true;
}

void dfs(int u, int v, int ls, int o) {
	if(o && ~d[v][u]) return;
	if(!o && ~d[u][v]) return;
	if(check(u, v, ls, o)) {
		if(o) d[u][v] = 0, d[v][u] = 1; 
		else d[u][v] = 1, d[v][u] = 0;
		return;
	}
	if(o) {
		bool f = true;
		for(int i = 0; i < n; i ++) {
			if(e[v][i] > ls) {
				dfs(u, i, e[v][i], ~o);
				if(d[u][i] == 1) f = false;
			}
		}
		if(f) d[v][u] = 1;
	} else {
		bool f = true;
		for(int i = 0; i < n; i ++) {
			if(e[u][i] > ls){
			   	dfs(i, v, e[u][i], ~o);
				if(d[v][i] == 1) f = false;
			}
		}
		if(f) d[u][v] = 1;
	}
}

int main() {
	scanf("%d%d", &n, &m);
	memset(e, -1, sizeof(e));
	memset(d, -1, sizeof(d));
	for(int i = 0; i < m; i ++) {
		int u, v; char w;
		scanf("%d%d%s", &u, &v, &w);
		u --, v --;
		e[u][v] = w-'a';
	}
	for(int i = 0; i < n; i ++) {
		for(int j = 0; j < n; j ++) {
			if(d[i][j]==-1) {
				dfs(i, j, -1, 0);
			}
		}
	}	
	for(int i = 0; i < n; i ++) {
		for(int j = 0; j < n; j ++) {
			if(d[i][j]) printf("A");
			else printf("B");
		}
		puts("");
	}
}
