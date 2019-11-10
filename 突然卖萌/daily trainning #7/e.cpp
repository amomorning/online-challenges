#include <bits/stdc++.h>

int main() {
	int n, X;
	double V;
	while(~scanf("%d%d%lf", &n, &X, &V)) {
		double Vy = 0;
		for(int i = 0; i < n; ++ i) {
			int l, r; 
			double v;
			scanf("%d%d%lf", &l, &r, &v); 
			Vy += v*(r-l)/X;
		}
		if(fabs(Vy) > V) puts("Too hard");
		else {
			double Vx = sqrt(V*V-Vy*Vy);
			if(Vx*2.0 < V) puts("Too hard");
			else printf("%.3f\n", 1.0*X/Vx);
		}
	}
}
