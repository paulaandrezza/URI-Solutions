#include <stdio.h>
 
int main() {
 
    float m[12][12], r=0;
    char c;
    int i, j;
    
    scanf("%c", &c);
    
    for(i=0 ; i<12 ; i++) {
    	for(j=0 ; j<12 ; j++) {
    		scanf("%f", &m[i][j]);
		}
	}
		
	for(i=1 ; i<11 ; i++) {
		if(i<=5) {
			for(j=0 ; j<i ; j++) {
				r += m[i][j];
			}
		} else {
			for(j=0 ; j<(11-i) ; j++) {
				r += m[i][j];
			}
		}
	}
		
	if(c == 'S') {
		printf("%.1f\n", r);	
	} else if (c == 'M') {
		printf("%.1f\n", r/30.0);
	}
	 	
    return 0;
}
