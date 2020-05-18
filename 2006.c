#include <stdio.h>
 
int main() {
 
    int t, c[5], i, p=0;
    
    scanf("%d", &t);
    
    for(i=0 ; i<5 ; i++) {
    	scanf("%d", &c[i]);
    	c[i] == t ? p++ :	 0;
	}
	
	printf("%d\n", p);
 
    return 0;
}
