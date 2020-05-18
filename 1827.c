#include <stdio.h>
 
int main() {
	
	int tam, i, j, div, meio, fim;
	
	while(scanf("%d", &tam) != EOF) {
			    
	    div = tam/3;
	    meio = (tam-1)/2;
	    fim = tam-div-1;
	    
	    int matriz[tam][tam];
	    
	    for(i=0 ; i<tam ; i++) {
	    	for(j=0 ; j<tam ; j++) {
	    		
	    		if(i>=div && j>=div && i<=fim && j<=fim) {	matriz[i][j] = 1;	}
	    		else if(i==j) {	matriz[i][j] = 2;	}
	    		else if(j==tam-i-1) {	matriz[i][j] = 3;	}
	    		else {	matriz[i][j] = 0;	}
	    		
	    		if(i==meio && j==meio) {	matriz[i][j] = 4;	}
	    		
			}
		}
	
	
	    for(i=0 ; i<tam ; i++) {
	    	for(j=0 ; j<tam ; j++) {
	    		printf("%d", matriz[i][j]);
	    	}
	    	printf("\n");
	    }	
	    
	    printf("\n");
		
	}
 
    return 0;
}
