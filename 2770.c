#include <stdio.h>
 
int main() {
 
    int x, y, m, a, b, i;
    
    while(scanf("%d %d %d", &x, &y, &m) == 3) {
    	
    	for (i=0 ; i<m ; i++) {
    		scanf("%d %d", &a, &b);
    		
    		if (a <= x && b <= y || a <= y && b <= x) {
    			printf("Sim\n");
			} else{
				printf("Nao\n");	
			}
		}
    	
	}
 
    return 0;
}
