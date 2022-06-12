#include <bits/stdc++.h>
using namespace std;

char s[4][110];

int l[4];
int get(int id) {
	for(int i = 0; s[id][i]; i ++) {
		if(s[id][i] == '.') return i+1;
	}
}

int main() {
	for(int i = 0; i < 4; i ++) {
		scanf("%s" ,s[i]);
		l[i] = strlen(s[i])-get(i);
	}
	int tot = 0;
	int ans[4];
	for(int i = 0; i < 4; i ++) {
		int f1 = 0, f2 = 0;
		for(int j = 0; j < 4; j ++) {
			if(l[i]*2 <= l[j]) f1++;
			if(l[i] >= l[j]*2) f2++;
		}
		if(f1 == 3 || f2 == 3) ans[tot++] = i;
	}
	if(tot == 1) printf("%c\n", ans[0]+'A');
	else puts("C");
}
