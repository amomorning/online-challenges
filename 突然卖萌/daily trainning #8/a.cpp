#include <bits/stdc++.h>

char s[110];

int main() {
	int t; scanf("%d", &t);
	while(t --) {
		scanf("%s", s);
		int a = 0, b = 0, c = 0;
		for(int i = 0; s[i]; ++ i) {
			if(s[i] == '@' || s[i] == '?' || s[i] == '!') a++;
			if(s[i] >= '0' && s[i] <= '9') b ++;
			if(s[i] >= 'a' && s[i] <= 'z') c ++;
			if(s[i] >= 'A' && s[i] <= 'Z') c ++;
		}
		if(a < 2) puts("The last character must be a symbol.");
		else if (b < 4) puts("The last character must be a digit.");
		else if (c < 4) puts("The last character must be a letter.");
		else puts("The last character can be any type.");
	}
}
