#include <stdio.h>
 
int main() {
 
    int i, t[4], n;
    
    for(i=0 ; i<4 ; i++) {
    	scanf("%d", &t[i]);
	}
	
	n = t[0] + t[1] + t[2] + t[3] - 3;
	
	printf("%d\n", n);
 
    return 0;
}
