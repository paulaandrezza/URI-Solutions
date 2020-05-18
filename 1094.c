#include <stdio.h>
 
int main() {
 
    int n, quantia, i, rato=0, sapo=0, coelho=0, total;
    char tipo;
 
 	scanf("%d", &n);
 	
 	for(i=0 ; i<n ; i++) {
 		scanf("%d %c", &quantia, &tipo);
 		
 		if(tipo == 'R') {
 			rato += quantia;
		} else if(tipo == 'S') {
			sapo += quantia;
		} else if(tipo == 'C') {
			coelho += quantia;
		}
			
	}
	
	total = rato+sapo+coelho;
	
	printf("Total: %d cobaias\n", total);
	printf("Total de coelhos: %d\n", coelho);
	printf("Total de ratos: %d\n", rato);
	printf("Total de sapos: %d\n", sapo);
	printf("Percentual de coelhos: %.2f %%\n", ((float)coelho*100.0/total));
	printf("Percentual de ratos: %.2f %%\n", ((float)rato*100.0/total));
	printf("Percentual de sapos: %.2f %%\n", ((float)sapo*100.0/total));
 	
    return 0;
}
