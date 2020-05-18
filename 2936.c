#include <stdio.h>
 
int main() {
 
    int porcoes[5] = {300, 1500, 600, 1000, 150};
    int qtdd[5], i, soma = 225;
    
    for(i=0 ; i<5 ; i++) {
    	scanf("%d", &qtdd[i]);
    	
    	soma = soma + qtdd[i] * porcoes[i];
    	
	}
	
	printf("%d\n", soma);
 
    return 0;
}
